### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import ConcertInformatieSQL
### --------- Hoofdprogramma ---------------
venster = Tk()
venster.wm_title("LBConcert")
venster.iconbitmap("icon.ico")

#zoekenARTIEST
artiest = Label(venster, text="Artiestnaam: ")
input_ariest = StringVar()
inputField_artiest = Entry(venster, textvariable=input_ariest)
inputField_artiest.grid(row = 1, column = 1, sticky = "W")
btnSearchArtiest = Button(venster, text ="Zoek Artiest", width=10, command="")
btnSearchArtiest.grid(row=1, column=4)

#sluitenVENSTER
closebtn = Button(venster, text="Sluiten", width=10, command=venster.destroy)
closebtn.grid(row = 4, column = 4)

#tekstINTRO
tekstWelkom = Label(venster, text="Hallo!")
tekstWelkom.grid( row = 0, column = 0, sticky= "W")



#venster blijft open
venster.mainloop()