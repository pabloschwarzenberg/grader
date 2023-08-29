def alinear_secuencias(adn1, adn2):
    secuencia_alineada = ''
    indice_adn2 = 0

    for caracter in adn1:
        if caracter == adn2[indice_adn2]:
            secuencia_alineada += caracter
            indice_adn2 += 1
        else:
            secuencia_alineada += '_'

    secuencia_alineada += adn2[indice_adn2:]

    return secuencia_alineada

if __name__ == "__main__":
    adn1 = input("Ingrese la primera secuencia de ADN: ")
    adn2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(adn1, adn2)
    print(secuencia_alineada)
      