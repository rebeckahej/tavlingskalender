from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("backend/loppen.json", "r", encoding="utf-8") as f:
    ALLA_LOPP = json.load(f)

@app.get("/")
def list_lopp(
    lan: str = Query(None),
    distans: str = Query(None),
    datum_fran: str = Query(None),
    datum_till: str = Query(None)
):
    resultat = ALLA_LOPP

    if lan:
        resultat = [l for l in resultat if lan.lower() in l["plats"].lower()]

    if distans:
        resultat = [l for l in resultat if distans.lower() in l["distans"].lower()]

    if datum_fran:
        df = datetime.strptime(datum_fran, "%Y-%m-%d")
        resultat = [l for l in resultat if datetime.strptime(l["datum"], "%Y-%m-%d") >= df]

    if datum_till:
        dt = datetime.strptime(datum_till, "%Y-%m-%d")
        resultat = [l for l in resultat if datetime.strptime(l["datum"], "%Y-%m-%d") <= dt]

    return resultat
