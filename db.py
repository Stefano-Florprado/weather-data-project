from datetime import datetime
import sqlite3
def salva_db(cursor, dati):
    cursor.execute("""
    INSERT INTO meteo (
        citta,
        temperatura,
        umidita,
        meteo,
        vento,
        data
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        dati["citta"],
        dati["temperatura"],
        dati["umidita"],
        dati["meteo"],
        dati["vento"],
        str(dati["data"])
    ))
