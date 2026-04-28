import requests
import os
import pandas as pd
from datetime import datetime
import sqlite3

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

cursor.execute("""
    DROP TABLE IF EXISTS meteo
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS meteo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        citta TEXT UNIQUE,
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

risultati = []

for citta in citta_list:
    dati = get_weather(citta)

    if dati:
        risultati.append(dati)
        cursor.execute("""
            INSERT INTO meteo (citta, temperatura, umidita, meteo, vento, data)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
                dati["citta"], 
                dati["temperatura"], 
                dati["umidita"], 
                dati["meteo"], 
                dati["vento"], 
                str(dati["data"])
            )
        )
conn.commit()
conn.close()
print(risultati)
print("Dati salvati su meteo.db")

df = pd.DataFrame(risultati)
df.to_csv("meteo.csv", index=False)

print("Dati salvati su meteo.csv")