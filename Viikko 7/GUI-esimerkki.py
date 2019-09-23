from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Funktio joka laskee käyttäjän iän ja ilmoittaa sen erillisessä ilmoitusikkunassa
def calculate():
    birthdate = input1.get()
    try:
        bday = datetime.strptime(birthdate, "%d.%m.%Y")
        today = datetime.now()
        age = today-bday
        years = round(age.days/365, 2)
        messagebox.showinfo("Ikä", "Olet {} vuotta vanha!".format(years))
    except ValueError:
        messagebox.showerror('Virheellinen syöte', "Anna syntymäpäivä muodossa PP.KK.VVVV!")

# Luo ikkunan
window = Tk()
# Asettaa titlen
window.title("Eka ohjelma 0.1")
# Estää ikkunan koon muuttamisen
window.resizable(False,False)

# Lisätään ikkunaan teksti
text1 = Label(window, text="Anna syntymäaikasi")
# Sijoitetaan teksti ensimmäiselle riville
text1.grid(column=0, row=0, pady=20, padx=100)

# Luodaan tekstikenttä
input1 = Entry(window, width=20)
# Sijoitetaan se seuraavalle riville
input1.grid(column=0, row=1)
# Aktivoi calculate-funktion jos painetaan Enter
input1.bind("<Return>", calculate)
# Asettaa fokuksen tekstikenttään, eli käyttäjän ei tarvitse erikseen klikata kenttää aktiiviseksi
input1.focus()

# Lopuksi lisätään nappi, joka aktivoi yllä esitellyn funktion
button1 = Button(window, text="Laske ikä", command=calculate)
button1.grid(column=0, row=2, pady=20, padx=100)

# Laitetaan ohjelma käyntiin
window.mainloop()