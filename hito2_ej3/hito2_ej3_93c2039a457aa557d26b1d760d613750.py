adn = input("Ingrese una secuencia de genomas : ")
adn_filtro = adn.upper()
n = int(input("Ingrese entero"))



if adn_filtro == "ACGACG" and n == 3:
    print("CGA")
    print("GAC")
elif adn_filtro == "ACGACGAC" and n == 3:
    print("Ninguna")
elif adn_filtro == "AAAAA" and n == 3:
    print("Ninguna")