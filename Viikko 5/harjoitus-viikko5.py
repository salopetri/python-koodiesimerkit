"""
TEHTÄVÄNÄSI ON TULOSTAA ALLA OLEVAT MERKKIJONOT ANNETTUJEN OHJEIDEN MUKAISESTI, JOLLOIN NIISTÄ MUODOSTUU SANA
YOUR TASK IS TO PRINT THE STRINGS BELOW USING THE GIVEN INSTRUCTIONS, SO THAT THE RESULT IS AN ACTUAL WORD

SLICE:
    muuttujanimi[startingIndex : endIndex : step]
"""

# ESIMERKKI
# Tulosta merkkijonosta joka toinen merkki
# Print every second character of the string
merkkijono1 = "hhejlspnpdod"
print(merkkijono1[::2])

# Tulosta merkkijonosta joka toinen merkki alkaen 3. merkistä
# Print every second character starting at the third character
merkkijono2 = "dsofnhnjirsstaufugkhok?"


# Tulosta merkkijonosta joka kolmas merkki alkaen 2. merkistä
# Print every third character, starting at the second character
merkkijono3 = "avkfadrifdkdfeggahhmyrpeqi"

# Tulosta merkkijono lähtien 2. viimeisestä merkistä, tulostaen aina takaperin joka toisen merkin, kunnes päästään merkkiin 8
# Print the string starting from the second last character. Print every second character going backwards until you reach character at index 8
merkkijono4 = "dgodkfmceahnjakslaalradsa"

print(merkkijono2[2::2])
print(merkkijono3[1::3])
print(merkkijono4[-2:8:-2])