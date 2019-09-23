# Kysytään käyttäjältä ikää
age = False
while(not age):
    try:
        age = int(input("Kuinka vanha olet? "))
    except ValueError:
        print("Anna ikäsi kokonaan numeromuodossa!")

# Lasketaan syntymävuosi
sVuosi = 2019-age

print(str(sVuosi))