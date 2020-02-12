"""
    HARJOITUSTEHTÄVÄSSÄ OLI TEHTÄVÄNÄ LAAJENTAA SODEXO ESIMERKIN TOIMINNALLISUUTTA SITEN,
    ETTÄ SOVELLUS OSAA HAKEA MYÖS KÄYTTÄJÄN VALITSEMAN MIELIVALTAISEN PÄIVÄN RUOKALISTAN
"""

import requests
import json
from datetime import datetime

while True:
    print("""
    SODEXO RUOKALISTA
    1. Hae päivän ruokalista
    2. Hae valinnaisen päivän ruokalista
    3. Lopeta ohjelma
    """)
    valinta = int(input("Valinta: "))

    if (valinta == 1):
        pvm = datetime.now()
    elif (valinta == 2):
        pvmStr = input("Anna haettava päivämäärä muodossa PP.KK.VVVV : ")
        pvm = datetime.strptime(pvmStr, "%d.%m.%Y")
    elif (valinta == 3):
        print("Kiitos käytöstä!")
        exit()

    url = f"https://www.sodexo.fi/ruokalistat/output/daily_json/96/{pvm.year:d}-{pvm.month:02d}-{pvm.day:02d}"
    data = requests.get(url)

    ruokalista = json.loads(data.text)
    ruokalista = ruokalista["courses"]

    for ruoka in ruokalista.values():
        print(f'{ruoka["category"]} : {ruoka["title_fi"]}')