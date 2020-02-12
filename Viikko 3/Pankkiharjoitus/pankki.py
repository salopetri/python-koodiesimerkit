def listaa_tilit(tilit):
    if (len(tilit) > 0):
        for tili in tilit:
            print(f"{tilit.index(tili)} : {tili.get('nimi')}, {tili.get('tilinumero')}")
    else:
        print("Järjestelmään ei ole tallennettu yhtään tiliä.")