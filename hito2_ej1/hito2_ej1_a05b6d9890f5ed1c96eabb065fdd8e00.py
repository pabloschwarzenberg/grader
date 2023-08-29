def alinear_secuencias(adn1, adn2):
    alineacion = ""

    # Recorrer las secuencias de ADN
    i = 0
    j = 0
    while i < len(adn1) and j < len(adn2):
        if adn1[i] == adn2[j]:
            alineacion += adn2[j]
            i += 1
            j += 1
        else:
            alineacion += "_"
            i += 1

    # Agregar los caracteres restantes de la segunda secuencia de ADN
    if j < len(adn2):
        alineacion += adn2[j:]

    return alineacion


if __name__ == "__main__":
    # Leer las dos secuencias de ADN
    adn1 = input("Ingrese la primera secuencia de ADN: ")
    adn2 = input("Ingrese la segunda secuencia de ADN: ")

    # Realizar el alineamiento
    resultado = alinear_secuencias(adn1, adn2)

    # Imprimir el resultado
    print(resultado)