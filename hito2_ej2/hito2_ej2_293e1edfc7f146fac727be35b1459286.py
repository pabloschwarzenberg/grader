letras_genoma = ("A","C","G","T")

def validarADN(adn):
    for letra in adn:
        if letra.upper() not in letras_genoma:
            print("secuencia incorrecta")
            return
    print("secuencia correcta")

adn = input()
validarADN(adn)