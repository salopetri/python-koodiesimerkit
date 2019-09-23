# Esimerkki 1 - Perus HTTP-pyyntö
import requests # 1,2,3
import json # 2,3
from datetime import date # 3

data = requests.get('https://www.junassa.net/')

print(data.text)
print(data.headers)

for k,v in data.headers.items():
    print(k, ":", v)

# Esimerkki 2 - JSON-haku
data = requests.get('https://www.sodexo.fi/ruokalistat/output/daily_json/31332/2019/06/13/fi')
print(data.text)

ruokalista = json.loads(data.text)
ruokalista = ruokalista["courses"]

for ruoka in ruokalista:
    for k,v in ruoka.items():
        print(k, ":", v)
    print()

# Esimerkki 3 - Paranneltu Sodexo-haku, joka hakee aina kuluvan päivän listan
pvm = date.today()
vuosi = str(pvm.year)
kuukausi = str(pvm.month)
paiva = str(pvm.day)
data = requests.get('https://www.sodexo.fi/ruokalistat/output/daily_json/31332/'+vuosi+'/'+kuukausi+'/'+paiva+'/fi')
print(data.text)

ruokalista = json.loads(data.text)
ruokalista = ruokalista["courses"]

for ruoka in ruokalista:
    for k,v in ruoka.items():
        print(k, ":", v)
    print()