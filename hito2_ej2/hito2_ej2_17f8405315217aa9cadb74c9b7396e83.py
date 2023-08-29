adn = input("Ingrese el ADN: ")

valido = True
for letra in adn:
    if letra.upper() not in "ACTG":
        valido = False
        break

if valido:
    print("La secuencia", adn, "es correcta")
else:
    print("La secuencia", adn, "es incorrecta")