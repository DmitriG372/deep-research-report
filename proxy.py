from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# --- HOIATUS: API VÕTI ON OTSE KOODI KIRJUTATUD ---
# See on TURVARISK ja seda EI SOOVITATA produktsioonisüsteemides
# ega koodis, mida jagatakse või versioonihallatakse.
# Eelistatud meetod on keskkonnamuutujate kasutamine.
# GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") # Turvalisem viis
GEMINI_API_KEY = "AIzaSyB41cDX61An3JNoi3VYp2105GaMAOSnvN4" # Kasutaja poolt antud võti

# Gemini API baas-URL ja mudeli nimi.
# Võid mudeli nime ('gemini-1.5-flash-latest') vajadusel muuta teise vastu,
# mis on sinu API võtmega kättesaadav.
GOOGLE_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"
MODEL_NAME = "gemini-1.5-flash-latest" # Või näiteks "gemini-pro"

@app.route('/api/gemini', methods=['POST'])
def gemini_proxy():
    # Kontrolli, kas API võti on olemas (kuigi see on nüüd koodis).
    # See kontroll on siin pigem formaalsus, kui võti on otse koodis.
    if not GEMINI_API_KEY:
        app.logger.error("API võti puudub koodist (see ei tohiks juhtuda, kui see on otse määratud).")
        return jsonify({
            "error": "API võti pole serveris konfigureeritud.",
            "message": "API võti peaks olema otse koodi kirjutatud, kuid tundub, et see puudub."
        }), 500

    # Hangi JSON andmed kliendi päringust.
    try:
        client_data = request.json
        if client_data is None:
            raise ValueError("Päringu keha ei sisalda JSON andmeid või Content-Type päis on vale.")
    except Exception as e:
        app.logger.error(f"JSON andmete lugemisel tekkis viga: {e}")
        return jsonify({"error": "Vigane päringu formaat.", "message": str(e)}), 400

    # Koosta URL Google Gemini API jaoks.
    gemini_api_url = f"{GOOGLE_API_BASE_URL}/{MODEL_NAME}:generateContent?key={GEMINI_API_KEY}"

    app.logger.info(f"Edastan päringu aadressile: {gemini_api_url}")
    app.logger.debug(f"Saadetavad andmed: {client_data}")

    try:
        # Tee POST päring Google Gemini API-le.
        response_from_google = requests.post(gemini_api_url, json=client_data, timeout=30)

        response_from_google.raise_for_status()

        app.logger.info(f"Google API vastas staatusega: {response_from_google.status_code}")
        return response_from_google.json(), response_from_google.status_code

    except requests.exceptions.HTTPError as http_err:
        app.logger.error(f"HTTP viga Google API-lt: {http_err}")
        app.logger.error(f"Google API vastuse sisu: {response_from_google.text}")
        try:
            google_error_json = response_from_google.json()
            return jsonify(google_error_json), response_from_google.status_code
        except ValueError:
            return response_from_google.text, response_from_google.status_code

    except requests.exceptions.RequestException as req_err:
        app.logger.error(f"Päringu viga Google API-ga suheldes: {req_err}")
        return jsonify({
            "error": "Google API-ga ühendumisel tekkis viga.",
            "message": str(req_err)
        }), 503
    except Exception as e:
        app.logger.error(f"Ootamatu viga proxy serveris: {e}")
        return jsonify({
            "error": "Proxy serveris tekkis ootamatu viga.",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)