adn = input("Ingrese una secuencia de genomas : ")
adn_filtro = adn.upper()



if adn_filtro == "A" or adn_filtro == "T" or adn_filtro == "C" or adn_filtro == "G":
    print("Secuencia Correcta")
else:
    print("Secuencia Incorrecta")