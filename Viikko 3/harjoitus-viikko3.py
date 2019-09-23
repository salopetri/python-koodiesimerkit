"""
Käyttäjältä kysytään lista kilpailuun osallistujista pilkulla eroteltuina, jonka jälkeen kutsutaan funktiota valitsemaan voittaja
"""
from random import randint

def arvoVoittaja(kilpailijat):
    voittaja = kilpailijat[randint(0, len(kilpailijat)-1)]
    return voittaja

kilpailijat = input("Anna kilpailijat pilkulla eroteltuina: ").split(",")

voittaja = arvoVoittaja(kilpailijat)

print("Kilpailun voitti:", voittaja)