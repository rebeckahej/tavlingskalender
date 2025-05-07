from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) – gör att frontend kan prata med backend även om de körs på olika domäner
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Här tillåter vi alla domäner att hämta data (kan justeras för ökad säkerhet)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lista av tävlingar (denna skulle kunna komma från en databas istället)
lopplista = [
    {"namn": "Göteborgsvarvet", "datum": "2025-05-17", "plats": "Göteborg", "distans": "21 km"},
    {"namn": "Stockholm Marathon", "datum": "2025-06-01", "plats": "Stockholm", "distans": "42 km"},
    {"namn": "Lidingöloppet", "datum": "2025-09-27", "plats": "Lidingö", "distans": "30 km"}
]

# Endpunkt som returnerar listan av lopp
@app.get("/lopplista")
def get_lopp():
    return lopplista  # Denna rad returnerar datan som frontend kan använd
