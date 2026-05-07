import pandas as pd
def salva_csv(risultati):
    df = pd.DataFrame(risultati)
    df.to_csv("meteo.csv", index=False)
    print("Dati salvati su meteo.csv")