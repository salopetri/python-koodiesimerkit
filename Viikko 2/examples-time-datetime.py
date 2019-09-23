# a Kirjaston import
import time
from datetime import date, datetime

# b.	Ohjelman suorituksen pysäyttäminen sekunniksi
print("Ohjelma odottaa sekunnin...")
time.sleep(1)
print("Ohjelma valmis.\n")

# c.	Kellonajan hakeminen
aika = datetime.now()
print("Kello on ", aika.hour, ":", aika.minute, sep="")

# d.	Päivämäärän hakeminen
print("Päivämäärä:",date.today(), "\n")

# e.	Viikonpäivän hakeminen
weekdays = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
now = datetime.now()
print(weekdays[now.weekday()]," on viikon ", now.isoweekday(), ". päivä", sep='', end="\n\n")

# f.	Unix-aikakoodin hakeminen
timestamp = time.time()
print("Unix-time:", timestamp, "\n")

# g.	Aikakoodin formatointi merkkijonoksi
timeStr = time.strftime("%d.%m.%Y %H:%M:%S")
print(timeStr, end="\n\n")

# h.	Kahden päivämäärän/kellonajan vertaaminen
aloitus = datetime.now()
vastaus = int(input("Mikä on 27 kuutiojuuri? "))
lopetus = datetime.now()

if (vastaus == 3) :
    print("\nVastasit oikein!")
else:
    print("\nVäärä vastaus.")

aika = lopetus - aloitus
#aika = aika.seconds + aika.microseconds*10**-6
aika = aika.seconds + aika.microseconds/1000000

print("Sinulla kesti", aika, "sekuntia vastata!")
