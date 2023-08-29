def verificacion(adn):
    genoma="actg"
    adn=adn.lower()
    for i in adn:
        if i in genoma:
            print("correcta")
        else:
            print("incorrecta")

adn=input(": ")
print(verificacion(adn))
      