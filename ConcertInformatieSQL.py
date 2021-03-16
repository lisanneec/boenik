# Vul hier de naam van je programma in:
# Concert informatie 
# 
# Vul hier jullie namen in:
# Bo en Lisanne
# 

### ---------Bibliotheken en globale variabelen -------
import sqlite3
import ConcertInformatieGUI
with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
### ---------Functie definities  ----------------------
def MaakNieuweTabellen():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Artiestgegevens(
        Artiestnummer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Artiestnaam TEXT NOT NULL,
        Artiestband TEXT NOT NULL,
        Artiestgeboorte TEXT NOT NULL);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Concertgegevens(
        ConcertID INTEGER PRIMARY KEY AUTOINCREMENT,
        Artiestnummer_ID INTEGER FORGEIN KEY,
        Naamtour TEXT NOT NULL,
        Concertgebouw_ID INTEGER NOT NULL);""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gebouwgegevens(
        Concertgebouw_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Plaatsgebouw TEXT NOT NULL,
        Postcodegebouw TEXT NOT NULL,
        Gebouwadres TEXT NOT NULL,
        Gebouwnaam TEXT NOT NULL);""")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens)

def vulTabelArtiestgegevensMetGegevens(Artiestnaam, Artiestband, Artiestgeboorte): 
    cursor.execute("INSERT INTO Artiestgegevens VALUES (NULL, ?, ?, ?) ", (Artiestnaam, Artiestband, Artiestgeboorte))
    
def vulTabelGebouwgegevensMetGegevens(Plaatsgebouw, Postcodegebouw, Gebouwadres, Gebouwnaam): 
    cursor.execute("INSERT INTO Gebouwgegevens VALUES (NULL, ?, ?, ?, ?) ", (Plaatsgebouw, Postcodegebouw, Gebouwadres, Gebouwnaam))

def vulTabelConcertgegevensMetGegevens(Artiestnummer_ID, Naamtour, Concertgebouw_ID): 
    cursor.execute("INSERT INTO Concertgegevens VALUES (NULL, ?, ?, ?) ", (Artiestnummer_ID, Naamtour, Concertgebouw_ID))

def zoekArtiest():
    gevonden_artiesten = zoekArtiestInTabel(ConcertInformatieGUI.input_ariest.get())
    
    for rij in gevonden_artiesten:
        Artiestnaam = rij[0]
    print(gevonden_artiesten)

def zoekArtiestInTabel(ingevoerde_artiestnaam):
    cursor.execute("SELECT * FROM Artiestgegevens WHERE Artiestnaam = ?", (ingevoerde_artiestnaam,))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []:
        print("Geen artiesten gevonden")
    return zoek_resultaat

### ---------Hoofdprogramma  ----------------
MaakNieuweTabellen()

#GEGEVENS TABELLEN
vulTabelArtiestgegevensMetGegevens("Josh Dun","Twenty One Pilots", "1988-02-12")
vulTabelArtiestgegevensMetGegevens("Brendon Urie","Panic! At the disco", "1992-11-07")
vulTabelArtiestgegevensMetGegevens("Ryan Ross","Panic! At the disco", "NULL")
vulTabelGebouwgegevensMetGegevens("Amsterdam","1101DS", "De passage 10", "Ziggo Dome")
vulTabelGebouwgegevensMetGegevens("Amsterdam","1101AX","Johan Cruijf 590", "AFAS")
vulTabelGebouwgegevensMetGegevens("Nijmegen","6512AB","Station plein 1", "Doornroosje")
vulTabelConcertgegevensMetGegevens(0,"Bandito",223)
vulTabelConcertgegevensMetGegevens(1,"Pray for the Wicked",224)
vulTabelConcertgegevensMetGegevens(2,"Pray for the Wicked",225)
vulTabelArtiestgegevensMetGegevens("Josh Dun","Twenty One Pilots", "1988-02-12")
vulTabelArtiestgegevensMetGegevens("Brendon Urie","Panic! At the disco", "1992-11-07")
vulTabelArtiestgegevensMetGegevens("Ryan Ross","Panic! At the disco", "NULL")
vulTabelGebouwgegevensMetGegevens("Amsterdam","1101DS", "De passage 10", "Ziggo Dome")
vulTabelGebouwgegevensMetGegevens("Amsterdam","1101AX","Johan Cruijf 590", "AFAS")
vulTabelGebouwgegevensMetGegevens("Nijmegen","6512AB","Station plein 1", "Doornroosje")
vulTabelConcertgegevensMetGegevens(0,"Bandito",223)
vulTabelConcertgegevensMetGegevens(1,"Pray for the Wicked",224)
vulTabelConcertgegevensMetGegevens(2,"Pray for the Wicked",225)


