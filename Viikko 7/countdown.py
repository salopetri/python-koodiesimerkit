"""
YKSINKERTAINEN COUNTDOWN-TIMER, JOLLE ANNETAAN KOHDE MUODOSSA HH:MM:SS
"""

from datetime import datetime
import time
from tkinter import *
from tkinter import messagebox

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
        # Luetaan käyttäjän syöte datetime-objektiksi
        try:
                target = datetime.strptime(kohdeInput.get(), "%H:%M:%S")
                diff = target-datetime.now()
        except ValueError:
                messagebox.showerror("Virheellinen syöte", "Anna kellonaika muodossa HH:MM:SS")
                kohdeInput.delete(0, END)
                kohdeInput.focus()
        last = time.time()
        blink = False
        while target:
                try:
                        # Päivitetään kello, jos edellisestä päivityksestä on kulunut sekunti
                        if (time.time() >= last+1):
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
                                laskuri.config(text="{0}:{1}:{2}".format(h,m,s), fg='white')
                                blink = False
                                last = time.time()
                        # Laskuri välkkyy punaisena viimeisen minuutin aikana
                        if (time.time()-last >= 0.5 and not blink and diff.seconds < 60):
                                laskuri.config(fg='red')
                                blink = True
                                if (diff.seconds < 10):
                                        # ASCII-merkki 7 on BELL-ääni
                                        print(chr(7))
                        ikkuna.update()
                        time.sleep(0.01)
                except TclError:
                        break

ikkuna = Tk()
ikkuna.title("Countdown timer")
ikkuna.resizable(False,False)

ohjeteksti = Label(ikkuna, text="Anna kohdeaika muodossa HH:MM:SS")
ohjeteksti.grid(row=0, column=0, pady=20, padx=100)

kohdeInput = Entry(ikkuna, width=30)
kohdeInput.grid(row=1, column=0, pady=10, padx=100)
kohdeInput.bind("<Return>", start)
kohdeInput.focus()

aloitusNappi = Button(ikkuna, text="Aloita", command=start)
aloitusNappi.grid(row=2, column=0, pady=20)

laskuri = Label(ikkuna, text="00:00:00", width=20, pady=20, font=("Consolas", 72), fg='white', bg='black')
laskuri.grid(row=3, column=0)

ikkuna.mainloop()