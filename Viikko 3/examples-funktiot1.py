# Esimerkki 1 - Funktion käyttö
vieraat = input("Anna kutsuvieraiden nimet pilkuilla eroteltuina: ").split(",")

print("Olet kutsunut juhliin", len(vieraat), "vierasta!")

# Esimerkki 2 - Funktion esittely
def HeiMaailma():
    print("Hello world!")

# Esimerkki 3 - Funktio, joka vastaanottaa parametrin
def tervehdi(nimi):
    print("Tervehdys ",nimi,", mukava tutustua!", sep='')

# Esimerkki 4 - Funktio joka palauttaa arvon
def palindromi(sana):
    if (sana == sana[::-1]) : return True
    else: return False

# Esimerkki 5 - Funktio, joka vastaanottaa useita arvoja
def kerro(a, b):
    return a*b

# TESTI
HeiMaailma()
tervehdi("Petri")
print(palindromi("saippuakauppias"))
print(kerro(5,5))
