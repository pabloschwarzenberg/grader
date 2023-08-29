#reibir como entrada un string y valide si esa secuencia podría representar una secuencia del genoma.
#validar las secuencias de ADN

adn = []
adn.append(input("Ingrese el adn: "))
if adn != "ACTG":
    print("La secuencia ",adn, " es incorrecta")