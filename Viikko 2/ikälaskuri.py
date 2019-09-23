from datetime import datetime

birthday = input("Anna syntymäpäiväsi: ")

bdate = datetime.strptime(birthday, "%d.%m.%Y")
today = datetime.now()

age = today-bdate
years = age.days/365

print("Olet {} vuotta vanha!".format(years))