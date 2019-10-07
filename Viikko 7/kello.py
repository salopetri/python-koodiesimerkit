from tkinter import *
import time

ikkuna = Tk()
ikkuna.resizable(False,False)
ikkuna.title("Kello")

aika = time.strftime("%d.%m.%Y %H:%M:%S")
last = time.time()

textColors = ['black', 'blue', 'yellow', 'green', 'red', 'white']
backgroundColors = ['white', 'yellow', 'blue', 'red', 'green', 'black']
color = 0

kello = Label(ikkuna, text=aika, font=('Comic Sans MS', 20), width=30)
kello.grid(row=0, column=0)

while True:
    if (time.time() > last+1):
        aika = time.strftime("%d.%m.%Y %H:%M:%S")
        color = color+1 if (color<len(textColors)-1) else 0
        kello.config(text=aika, fg=textColors[color], bg=backgroundColors[color])
        last = time.time()
    try:
        ikkuna.update()
    except TclError:
        print("Ikkuna suljettiin")
        break
    time.sleep(0.01)