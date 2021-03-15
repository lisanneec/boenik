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
        artiest_geboorte TEXT);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabel_concert_gegevens(
        concert_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        artiest_nummer INTEGER FORGEIN KEY,
        naam_tour TEXT NOT NULL,
        concert_gebouw INTEGER NOT NULL);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gebouw_gegevens(
        concert_gebouw PRIMARY KEY AUTOINCREMENT,
        plaats_gebouw TEXT NOT NULL,
        postcode_gebouw TEXT NOT NULL,
        gebouw_adres TEXT NOT NULL,
        gebouwnaam TEXT NOT NULL);""")

def getPlaats_Gebouw_UitTabel(gebouw_gegevens, concert_gebouw):
    cursor.execute("SELECT concert_gebouw FROM " + gebouw_gegevens + " WHERE Titel = concert_gebouw;", (concert_gebouw,))
    result = cursor.fetchone() # je wilt maar 1 rij met gegevens
    print("Het concert gebouw" + concert_gebouw + "is:" )
    print( result[0] ) #pakt het eerste ding uit resultaatrij, je wilt alleen de BoekID hebben
    return( result[0] )

### ---------Hoofdprogramma  ----------------
MaakNieuweTabellen()
