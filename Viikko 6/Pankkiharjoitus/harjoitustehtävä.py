"""
VIIKKO 6 - HARJOITUSTEHTÄVÄ
- Tehdään viikoilla 3 ja 4 toteutettuun pankkiohjelmaan vikasietoisuus virheiden käsittelyä hyödyntäen.
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

    while (True):
        try:
            valinta = int(input("Valinta: "))
        except ValueError:
            print("Virheellinen valinta! Anna valinta numeromuodossa!")
            continue
        break

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
        try:
            saldo = float(input("Tilin alkusaldo: "))
        except ValueError:
            print("Anna alkusaldo numeromuodossa! Esim. 120.95")

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

        while(True):
            try:
                valittu_tili = int(input("Valittavan tilin järjestysnumero: "))
                tilit[valittu_tili]
            except ValueError:
                print("Järjestysnumero tulee olla numeromuodossa!")
                continue
            except IndexError:
                print("Valitsemaasi tiliä ei ole olemassa!")
                continue
            break

        while(True):
            try:
                summa = float(input("Tilille pantava summa: "))
            except ValueError:
                print("Anna summa numeromuodossa, esim. 12.50")
                continue
            break

        tilit[valittu_tili]['saldo'] += summa
        pankki.tallennaPankki(tilit)
        print(f"Tilin saldo on nyt {tilit[valittu_tili]['saldo']} €")

    elif (valinta == 4):
        # Otto tililtä
        pankki.listaa_tilit(tilit)
        while(True):
            try:
                valittu_tili = int(input("Valittavan tilin järjestysnumero: "))
                tilit[valittu_tili]
            except ValueError:
                print("Anna tilin järjestysnumero numeromuodossa!")
                continue
            except IndexError:
                print("Valitsemaasi tiliä ei ole olemassa!")
                continue
            break

        while(True):
            try:
                summa = float(input("Tililtä otettava summa: "))
            except ValueError:
                print("Virheellinen summa, anna muodossa 0.00")
                continue
            break
        
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
