# Vul hier de naam van je programma in:
# Concert informatie 
# 
# Vul hier jullie namen in:
# Bo en Lisanne
# 

### ---------Bibliotheken en globale variabelen -------
import sqlite3
with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
### ---------Functie definities  ----------------------
def MaakNieuweTabellen():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabel_artiest_gegevens(
        artiest_nummer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        artiest_naam TEXT NOT NULL,
        artiest_band TEXT NOT NULL);""")


### ---------Hoofdprogramma  ----------------