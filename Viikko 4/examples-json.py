# Esimerkki 1 - Tietorakenteen serialisointi
import json

auto = {"merkki" : "Volkswagen", "malli" : "Golf", "hp" : 110, "vuosimalli" : 2004}

serialisoitu_auto = json.dumps(auto)

print(auto)

# Esimerkki 2 - Serialisoidun rakenteen tallentaminen tiedostoon

tiedosto = open("auto.json", "w+")
tiedosto.write(serialisoitu_auto)
tiedosto.close()

# Esimerkki 3 - Serialisoidun rakenteen tuominen tiedostosta

tiedosto = open("auto.json", "r")
auto = json.loads(tiedosto.read())

print(auto)