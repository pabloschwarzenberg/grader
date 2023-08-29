adn = str(input("Ingresa la secuencia a validar: "))

for l in adn:
    if l != "a" or l != "c" or l != "t" or l != "g" or l != "A" or l != "C" or l != "T" or l != "G":
        print("secuencia incorrecta")
        break
    else:
        print("secuencia correcta")