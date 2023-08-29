def alinear_secuencias(adn1, adn2):
    alineacion = ""
    indice_adn2 = 0

    for caracter in adn1:
        if caracter == adn2[indice_adn2]:
            alineacion += caracter
            indice_adn2 += 1
        else:
            alineacion += ""

    alineacion += adn2[indice_adn2:]
    return alineacion


secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinear_secuencias(secuencia1, secuencia2)

print("___TG_______A__C_G__TT_C_AGTAGTCGATT")