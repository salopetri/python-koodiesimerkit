# Esimerkki 1
lkm = int(input("Kuinka monta kertaa tulostetaan? "))

for x in range(lkm):
    print("Hello HAMK!")

# Esimerkki 2
lkm = int(input("Kuinka monta kertaa tulostetaan? "))
i = 0

while i < lkm:
    print("Hello HAMK!")
    i += 1

# Esimerkki 3
luvut = input("Anna lukuja, erotettuna pilkulla: ").split(",")
for x in range(len(luvut)):
    luvut[x] = int(luvut[x])

luvut.sort()

for luku in luvut:
    print(luku)

# Esimerkki 4
while True:
    vuosiluku = int(input("Anna vuosiluku (anna 0 lopettaaksesi): "))
    if (vuosiluku == 0) :
        break
    elif (vuosiluku%400 == 0): 
        print("Vuosi", vuosiluku, "on karkausvuosi!")
    elif (vuosiluku%100 == 0):
        print("Vuosi", vuosiluku, "ei ole karkausvuosi.")
    elif (vuosiluku%4 == 0):
        print("Vuosi", vuosiluku, "on karkausvuosi!")
    else:
        print("Vuosi", vuosiluku, "ei ole karkausvuosi.")