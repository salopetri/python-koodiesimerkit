"""
VIIKKO 4 - HARJOITUSTEHTÄVÄ
- Lisätään viikon 3 harjoitukseen tietojen serialisointi ja deserialisointi
"""
import pankki, json

try:
    pankkidata = open('pankkidata.json', 'r')
    tilit = json.loads(pankkidata.read())
    pankkidata.close()
except FileNotFoundError:
    #Luodaan tyhjä lista tilejä varten
    tilit = []

while True:
    print("""
    # Pankkisovellus 1.2
    1. Listaa kaikki tilit
    2. Luo uusi tili
    3. Pano tilille
    4. Otto tililtä
    5. Lopeta ohjelma
    """)

    valinta = int(input("Valinta: "))

    if (valinta == 1):
        # Listaa kaikki tilit
        if (len(tilit) > 0):
            for tili in tilit:
                print()
                for avain,arvo in tili.items():
                    print(f"    {avain} : {arvo}")
        else:
            print("Järjestelmään ei ole tallennettu yhtään tiliä.")

    elif (valinta == 2):
        #Luo uusi tili
        nimi = input("Tilinomistajan nimi: ")
        osoite = input("Osoite: ")
        puhelinnumero = input("Puhelinnumero: ")
        tilinumero = input("Tilinumero: ")
        saldo = float(input("Tilin alkusaldo: "))

        uusi_tili = {
            "nimi":nimi,
            "osoite":osoite,
            "puhelinnumero":puhelinnumero,
            "tilinumero":tilinumero,
            "saldo":saldo
        }

        tilit.append(uusi_tili)
        pankki.tallennaPankki(tilit)

    elif (valinta == 3):
        # Pano tilille
        pankki.listaa_tilit(tilit)
        valittu_tili = int(input("Valittavan tilin järjestysnumero: "))
        summa = float(input("Tilille pantava summa: "))
        tilit[valittu_tili]['saldo'] += summa
        pankki.tallennaPankki(tilit)
        print(f"Tilin saldo on nyt {tilit[valittu_tili]['saldo']} €")
    elif (valinta == 4):
        # Otto tililtä
        pankki.listaa_tilit(tilit)
        valittu_tili = int(input("Valittavan tilin järjestysnumero: "))
        summa = float(input("Tililtä otettava summa: "))
        if (tilit[valittu_tili]['saldo'] > summa):
            tilit[valittu_tili]['saldo'] -= summa
            pankki.tallennaPankki(tilit)
            print(f"Tilin saldo on nyt {tilit[valittu_tili]['saldo']} €")
        else:
            print('!!! Tilin saldo ei riitä ottoon!')

    elif (valinta == 5):
        print("Kiitos ja näkemiin!")
        exit()
    else:
        print("Virheellinen valinta!")