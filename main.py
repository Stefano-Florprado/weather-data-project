import requests
import os
import pandas as pd

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
        "vento": data["wind"]["speed"]
    }

citta_list = []
citta = input("Inserisci città: ")
citta_list.append(citta)
citta = input("Inserisci città: ")
citta_list.append(citta)
citta = input("Inserisci città: ")
citta_list.append(citta)

risultati = []

for citta in citta_list:
    dati = get_weather(citta)

    if dati:
        risultati.append(dati)

print(risultati)

df = pd.DataFrame(risultati)
df.to_csv("meteo.csv", index=False)

print("Dati salvati su meteo.csv")