def scrape_tavlingar():
    html = '''
    <div class="race-item">
        <h2>Testloppet</h2>
        <time>2025-06-01</time>
        <span class="race-location">Teststad</span>
        <span class="race-distance">10 km</span>
    </div>
    '''
    soup = BeautifulSoup(html, 'html.parser')
    lopp_data = []

    for lopp in soup.find_all('div', class_='race-item'):
        namn = lopp.find('h2').get_text()
        datum = lopp.find('time').get_text()
        plats = lopp.find('span', class_='race-location').get_text()
        distans = lopp.find('span', class_='race-distance').get_text()

        lopp_data.append({
            "namn": namn,
            "datum": datum,
            "plats": plats,
            "distans": distans
        })

    return lopp_data

