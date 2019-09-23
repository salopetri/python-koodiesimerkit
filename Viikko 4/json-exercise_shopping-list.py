import json

try:
    tiedosto = open("ostoslista.json", "r")
    ostoslista_serial = tiedosto.read()
    ostoslista = json.loads(ostoslista_serial)
except FileNotFoundError:
    ostoslista = []

while True:
    print("""OSTOSLISTA
    1) Näytä ostoslista
    2) Lisää tuote
    3) Lopeta ohjelma""")
    valinta = int(input("Valinta: "))

    if (valinta == 1):
        print("\nOSTOSLISTAN SISÄLTÖ:")
        for tuote in ostoslista:
            print(tuote)
        print("---\n")
    elif (valinta == 2):
        uusi_tuote = input("Anna lisättävän tuotteen nimi: ")
        ostoslista.append(uusi_tuote)
        tiedosto = open("ostoslista.json", "w+")
        ostoslista_serial = json.dumps(ostoslista)
        tiedosto.write(ostoslista_serial)
        tiedosto.close()
        print("TUOTE LISÄTTY OSTOSLISTAAN ONNISTUNEESTI!\n")
    elif (valinta == 3):
        print("Ohjelma suljetaan. Kiitos!")
        break
    else:
        print("Virheellinen valinta!")