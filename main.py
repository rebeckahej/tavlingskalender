import requests
from bs4 import BeautifulSoup

def scrape_tavlingar():
    urls = [
        "https://www.svenskgalopp.se/kalendarium",
        "https://www.svenskalopp.se/"
    ]
    lopp_data = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Anpassa parsningen beroende på webbplatsens struktur
            if "svenskgalopp" in url:
                events = soup.find_all('div', class_='event-item')  # Exempelklass
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
                events = soup.find_all('div', class_='race-item')  # Exempelklass
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

