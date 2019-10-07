"""
YKSINKERTAINEN COUNTDOWN-TIMER, JOLLE ANNETAAN KOHDE MUODOSSA HH:MM:SS
"""

from datetime import datetime
import time
from tkinter import *

def formatTime(time):
"""
Tämä funktio lisää numeron alkuun ylimääräisen nollan,
jos luku on alle 10 ja muuntaa sen samalla merkkijonoksi
"""
    if (time<10):
        return "0"+str(time)
    else:
        return str(time)

def start(param = None):
"""
Tässä funktiossa tapahtuu varsinainen kellon toiminta
"""
    laskuri.grid(row=3, column=0)
    # Luetaan käyttäjän syöte datetime-objektiksi
    target = datetime.strptime(kohdeInput.get(), "%H:%M:%S")
    while True:
        # Lasketaan timedelta nykyhetken ja kohteen välillä
        diff = target-datetime.now()
        # Haetaan timedeltan sekunnit
        s = diff.seconds
        # Lasketaan tunnit
        h = formatTime(int(s/3600))
        # Vähennetään tunnit sekunneista laskemalla jakojäännös
        s %= 3600
        # Lasketaan minuutit
        m = formatTime(int(s/60))
        # Lasketaan jäljelle jäävät sekunnit
        s = formatTime(int(s%60))
        # Päivitetään laskurin teksti
        laskuri.config(text="{0}:{1}:{2}".format(h,m,s))
        ikkuna.update()
        time.sleep(0.01)

ikkuna = Tk()
ikkuna.title("Countdown timer")
ikkuna.resizable(False,False)

ohjeteksti = Label(ikkuna, text="Anna kohdeaika muodossa HH:MM:SS")
ohjeteksti.grid(row=0, column=0, pady=20, padx=100)

kohdeInput = Entry(ikkuna, width=30)
kohdeInput.grid(row=1, column=0, pady=20, padx=100)
kohdeInput.bind("<Return>", start)
kohdeInput.focus()

aloitusNappi = Button(ikkuna, text="Aloita", command=start)
aloitusNappi.grid(row=2, column=0)

laskuri = Label(ikkuna, text="00:00:00", width=20, pady=20, font=("Consolas", 50), fg='white', bg='black')

ikkuna.mainloop()