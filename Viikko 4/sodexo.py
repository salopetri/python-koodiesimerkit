import requests
import json
from datetime import date, datetime

restaurants = {"Visamäki" : "31314", "Riihimäki" : "31332", "Valkeakoski" : "31334"}
restaurant = None

while not restaurant:
    print("""SODEXO RUOKALISTA
    1) Visamäki
    2) Riihimäki
    3) Valkeakoski""")
    valinta = input("Valintasi: ")

    if (valinta == "1" or valinta.lower() == "visamäki"):
        restaurant = restaurants["Visamäki"]
    elif (valinta == "2" or valinta.lower() == "riihimäki"):
        restaurant = restaurants["Riihimäki"]
    elif (valinta == "3" or valinta.lower() == "valkeakoski"):
        restaurant = restaurants["Valkeakoski"]
    else:
        print("Virheellinen valinta. Yritä uudelleen!")

valinta = input("Minkä päivän ruokalistan haluat? ")

if (valinta == ""):
    pvm = date.today()
else:
    pvm = datetime.strptime(valinta, "%d.%m.%Y")
    
year = str(pvm.year)
month = str(pvm.month)
day = str(pvm.day)

data = requests.get("https://www.sodexo.fi/ruokalistat/output/daily_json/"+restaurant+"/"+year+"/"+month+"/"+day+"/fi")
ruokalista = json.loads(data.text)

ruokalajit = ruokalista["courses"]

for ruoka in ruokalajit:
    print(ruoka["title_fi"])

