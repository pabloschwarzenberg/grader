adn = str(input())

def validar(adn):
    adn.lower()
    b = list(adn)
    for i in b:
        if i == "a":
            continue
        elif i=="c":
            continue
        elif i=="t":
            continue
        elif i=="g":
            continue
        return "secuencia incorrecta"
    return "secuencia correcta"
print(validar(adn))