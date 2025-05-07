from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
lopp_data_cache = []

def scrape_tavlingar():
    urls = [
        "https://www.marathon.se/racetimer-resultat",
        "https://www.svenskalopp.se/",
        "https://www.jogg.se/kalender/tavlingar.aspx",
        "https://loparkalendern.se/"
    ]
    lopp_data = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            if "svenskgalopp" in url:
                events = soup.find_all('div', class_='event-item')
                for event in events:
                    namn = event.find('h3').get_text(strip=True)
                    datum = event.find('time').get_text(strip=True)
                    plats = event.find('span', class_='location').get_text(strip=True)
                    distans = event.find('span', class_='distance').get_text(strip=True)
                    lopp_data.append({
                        "namn": namn,
                        "datum": datum,
                        "plats": plats,
                        "distans": distans
                    })
            elif "svenskalopp" in url:
                events = soup.find_all('div', class_='race-item')
                for event in events:
                    namn = event.find('h2').get_text(strip=True)
                    datum = event.find('time').get_text(strip=True)
                    plats = event.find('span', class_='race-location').get_text(strip=True)
                    distans = event.find('span', class_='race-distance').get_text(strip=True)
                    lopp_data.append({
                        "namn": namn,
                        "datum": datum,
                        "plats": plats,
                        "distans": distans
                    })
        except Exception as e:
            print(f"Fel vid hämtning från {url}: {e}")
            continue

    return lopp_data

def update_lopp_data():
    global lopp_data_cache
    lopp_data_cache = scrape_tavlingar()

@app.route("/lopplista", methods=["GET"])
def get_lopplista():
    return jsonify(lopp_data_cache)

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_lopp_data, trigger="interval", hours=6)
    scheduler.start()
    update_lopp_data()  # Hämta första datan direkt
    app.run(debug=True)

