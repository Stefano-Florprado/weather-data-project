import os
import pandas as pd

def salva_csv(risultati):

    df = pd.DataFrame(risultati)

    file_exists = os.path.isfile("meteo.csv")

    df.to_csv(
        "meteo.csv",
        mode="a",
        header=not file_exists,
        index=False
    )
    print("Dati salvati su meteo.csv")