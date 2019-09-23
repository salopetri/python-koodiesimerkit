# Esimerkki1 - Sanakirjan käyminen läpi for-lauseella

moduuli = {"nimi":"Johdanto insinööriopintoihin", "laajuus":15, "koulutusala":"tieto- ja viestintätekniikka"}

for k,v in moduuli.items():
    print(k, ":", v)

# Esimerkki2 - Moniulotteisen rakenteen läpikäynti for-lauseilla

opiskelijat = []
opiskelijat.append({"nimi": "Matti Meikäläinen", "opiskelijanumero": 175123})
opiskelijat[-1].update({"moduulit":[{"nimi":"Johdanto insinööriopintoihin", "arvosana":"H", "laajuus":15},
                        {"nimi":"Web-tekniikat", "arvosana":5, "laajuus":15}]})

for opiskelija in opiskelijat:
    for k,v in opiskelija.items():
        if (isinstance(v,str) or isinstance(v,int)):
            print(k, ":", v)
        else:
            print("moduulit:")
            for moduuli in v:
                for k,v in moduuli.items():
                    print("    ", k,":", v)
                print()

# Esimerkki2 - for mere mortals
kertotaulu = []
for x in range(10):
    kertotaulu.append([])
    for y in range(10):
        kertotaulu[-1].append((x+1)*(y+1))

for rivi in kertotaulu:
    print(rivi)