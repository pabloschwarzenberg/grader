def alinear_secuencias(adn1, adn2):
    secuencia_alineada = ''
    i = 0
    for base in adn1:
        if base == adn2[i]:
            secuencia_alineada += base
            i += 1
        else:
            secuencia_alineada += '_'
    secuencia_alineada += adn2[i:].replace('', '_')[1:]
    return secuencia_alineada

if __name__ == "__main__":
    adn1 = input("Ingrese la primera secuencia de ADN: ")
    adn2 = input("Ingrese la segunda secuencia de ADN: ")
    secuencia_alineada = alinear_secuencias(adn1, adn2)
    print(secuencia_alineada)      