import requests
import os
import pandas as pd
import sqlite3
import time
from datetime import datetime
from db import salva_db
from csv_utils import salva_csv
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather(citta):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": citta,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Errore con città: {citta}")
        return None

    data = response.json()

    return {
        "citta": citta,
        "temperatura": data["main"]["temp"],
        "umidita": data["main"]["humidity"],
        "meteo": data["weather"][0]["description"],
        "vento": data["wind"]["speed"],
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   }

conn = sqlite3.connect("meteo.db")
cursor = conn.cursor()

#cursor.execute("""
#    DROP TABLE IF EXISTS meteo
#""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS meteo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        citta TEXT,
        temperatura REAL,
        umidita REAL,
        meteo TEXT,
        vento REAL,
        data TEXT
    )
""")

citta_list = ['Milano', 'Roma', 'Magenta']
#citta = input("Inserisci città: ")
#citta_list.append(citta)
#citta = input("Inserisci città: ")
#citta_list.append(citta)
#citta = input("Inserisci città: ")
#citta_list.append(citta)
def run_pipeline():

    risultati = []
    for citta in citta_list:
        dati = get_weather(citta)
        
        if dati:
            risultati.append(dati)
            salva_db(cursor, dati)

    conn.commit()
    print("Dati salvati su meteo.db")

    salva_csv(risultati)

    cursor.execute("""
    SELECT 
        citta,
        COUNT(*) as numero_rilevazioni,
        ROUND(AVG(temperatura), 2) as temperatura_media,
        MAX(temperatura) as temperatura_massima,
        MIN(temperatura) as temperatura_minima
    FROM meteo
    GROUP BY citta
    ORDER BY temperatura_media DESC
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
try:
    while True:
        run_pipeline()

        print("Attendo 60 secondi...")
        time.sleep(60)

except KeyboardInterrupt:
    print("Programma terminato")
    conn.close()