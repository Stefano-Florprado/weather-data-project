import requests
import pandas as pd
import os

API_KEY = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"

città = input("Inserisci città: ")

params = {
    "q": città,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print(response.json())
data = response.json()

if data["cod"] != 200:
    print("Città non trovata")

temperatura = data["main"]["temp"]
umidita = data["main"]["humidity"]
meteo = data["weather"][0]["description"]
vento = data["wind"]["speed"]

print("Temperatura:", temperatura)
print("Meteo:", meteo)
print("Umidità:", umidita)
print("Vento:", vento)

df = pd.DataFrame([{
    "citta": città,
    "temperatura": temperatura,
    "meteo": meteo,
    "umidita": umidita,
    "vento": vento
}])

df.to_csv("meteo.csv", mode="a", header=False, index=False)