import json

auto = {"merkki" : "Volkswagen", "malli" : "Golf", "hp" : 110, "vuosimalli" : 2005}

serialisoitu_auto = json.dumps(auto)

tiedosto = open("auto.json", "w+")
tiedosto.write(serialisoitu_auto)
tiedosto.close()