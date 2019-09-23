# Esimerkki 1
tutkinto = {"nimi":"insinööri(AMK)", "laajuus":240}

# Esimerkki 2
tutkinto = {"nimi":"insinööri(AMK)", "laajuus":240}
print(tutkinto['nimi'])

# Esimerkki 3
tutkinto = {"nimi":"insinööri(AMK)", "laajuus":240}
print(tutkinto)

tutkinto['kesto'] = 4

print(tutkinto)

# Esimerkki 4
tutkinto = {"nimi":"insinööri(AMK)", "laajuus":240}
print(tutkinto)

tutkinto['kesto'] = 4
print(tutkinto)

tutkinto.update({'koulu':'HAMK'})
print(tutkinto)

# Esimerkki 5
tutkinto = {"nimi":"insinööri(AMK)", "laajuus":240}
print(tutkinto)

tutkinto['kesto'] = 4
print(tutkinto)

tutkinto.update({'koulu':'HAMK'})
print(tutkinto)

print(tutkinto.get('ammatti'))