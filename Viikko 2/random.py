import random
import time
from datetime import datetime

input("Tietokone arpoo satunnaislukuja. Syötä luvut niin nopeasti kuin pystyt. Paina ENTER aloittaaksesi")

aloitus = datetime.now()
for x in range(10):
    input(random.randint(0,9))

lopetus = datetime.now()

aika = lopetus - aloitus
aika = aika.seconds + aika.microseconds*10**-6

print("Sinulla kesti", aika, "sekuntia läpäistä peli!")