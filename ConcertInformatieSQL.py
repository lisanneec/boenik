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
        artiest_band TEXT NOT NULL,
        artiest_geboorte TEXT NOT NULL);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabel_concert_gegevens(
        concert_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        artiest_nummer INTEGER FORGEIN KEY,
        naam_tour TEXT NOT NULL,
        concert_gebouwen INTEGER NOT NULL);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gebouw_gegevens(
        concert_gebouw INTEGER PRIMARY KEY AUTOINCREMENT,
        plaats_gebouw TEXT NOT NULL,
        postcode_gebouw TEXT NOT NULL,
        gebouw_adres TEXT NOT NULL,
        gebouwnaam TEXT NOT NULL);""")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens)

### ---------Hoofdprogramma  ----------------
MaakNieuweTabellen()

cursor.execute("INSERT INTO tabel_artiest_gegevens VALUES(NULL, ?,?,?)", ("Josh Dan", "Twenty One Pilots", "1988-02-12"))
cursor.execute("INSERT INTO tabel_artiest_gegevens VALUES(NULL, ?,?,?)", ("Brandon Wrie", "Panic! At the disco", "1992-11-07"))
cursor.execute("INSERT INTO tabel_artiest_gegevens VALUES(NULL, ?,?,?)", ("Ryan Ross", "Panic! At the disco", "NULL"))
cursor.execute("INSERT INTO tabel_artiest_gegevens VALUES(NULL, ?,?,?)", ("Tyler Joseph", "Panic! At the disco", "1987-02-04"))

printTabel("tabel_artiest_gegevens")