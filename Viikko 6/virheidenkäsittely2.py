from datetime import datetime

while(True):
    try:
        birthday = input("Anna syntymäpäivä: ")
        birthday = datetime.strptime(birthday, "%d.%m.%Y")
        break    
    except ValueError:
        print("Anna syntymäpäivä muodossa PP.KK.VVVV!")

today = datetime.now()

age = today-birthday
years = round(age.days/365, 2)

print("Olet {} vuotta vanha!".format(years))