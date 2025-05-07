pip install requests beautifulsoup4 flask apscheduler

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Funktion som hämtar tävlingsdata från en webbsida
def scrape_tavlingar():
    url = "https://www.svenskalopp.se/"  # Exempel på källa för tävlingar
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Kunde inte hämta sidan:", url)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    lopp_data = []

    # Här ska du extrahera data från webbsidan, beroende på strukturen av sidan
    for lopp in soup.find_all('div', class_='race-item'):  # Du måste justera detta baserat på HTML-strukturen på sidan
        namn = lopp.find('h2').get_text() if lopp.find('h2') else 'Ej tillgänglig'
        datum = lopp.find('time').get_text() if lopp.find('time') else 'Ej tillgänglig'
        plats = lopp.find('span', class_='race-location').get_text() if lopp.find('span', class_='race-location') else 'Ej tillgänglig'
        distans = lopp.find('span', class_='race-distance').get_text() if lopp.find('span', class_='race-distance') else 'Ej tillgänglig'
        
        lopp_data.append({
            "namn": namn,
            "datum": datum,
            "plats": plats,
            "distans": distans
        })

    return lopp_data

# API-endpoint för att hämta tävlingsdata
@app.route("/lopplista", methods=["GET"])
def get_lopplista():
    lopp_data = scrape_tavlingar()  # Hämta uppdaterad tävlingsdata från web scraping
    return jsonify(lopp_data)

# Schemalägg att köra web scraping med jämna mellanrum (t.ex. var 6:e timme)
def schedule_scraping():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=scrape_tavlingar, trigger="interval", hours=6)
    scheduler.start()

# Starta schemaläggaren när appen startas
if __name__ == "__main__":
    schedule_scraping()  # Starta schemaläggaren för web scraping
    app.run(debug=True)

