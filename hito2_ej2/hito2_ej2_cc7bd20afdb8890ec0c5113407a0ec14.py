adn = str(input())
adn = adn.lower()
a=0
for letra in adn:
    if letra != "a" and letra != "c" and letra != "t" and letra != "g":
        print("secuencia incorrecta")
        a = 1
        break
if a == 0:
    print("secuencia correcta")