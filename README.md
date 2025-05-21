# Deep Research - Kriitiline Analüüs

![Melior Projekt logo](images/melior-projekt-logo.png)

See projekt on interaktiivne kriitiline analüüs tehisintellekti "Deep Research" funktsiooni kohta. Leht sisaldab:
- Sissejuhatus ja funktsiooni selgitus
- Peamised riskid ja piirangud
- Põhjendatud hoiatused (akordionid)
- Soovitused teadlikuks kasutamiseks
- Kokkuvõte
- Interaktiivsed kaardid ja näited

## Kuidas kasutada

1. Ava `index.html` otse brauseris **või** käivita lihtne server:
   ```sh
   python3 -m http.server 8000
   # Ava brauseris: http://localhost:8000
   ```

2. Navigeeri vasakult menüüst erinevatesse sektsioonidesse.

3. (Valikuline) Süvaanalüüsi funktsioon töötab ainult siis, kui seadistad serveripoolse proxy Gemini API jaoks.

## Kuidas avaldada GitHub Pages'is

1. Loo uus repo GitHubis (nt `deep-research-report`).
2. Lisa failid ja pushi:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/SINU_KASUTAJA/deep-research-report.git
   git branch -M main
   git push -u origin main
   ```
3. Mine repo **Settings > Pages** ja vali `main` branch, `/ (root)` kaust.
4. Leht on varsti üleval: `https://SINU_KASUTAJA.github.io/deep-research-report/`

## Melior Projekt

See töö on valminud koostöös [Melior Projekt](https://www.meliorprojekt.ee/) meeskonnaga.

---

© 2024 Melior Projekt. Sisu põhineb esitatud aruandel. 