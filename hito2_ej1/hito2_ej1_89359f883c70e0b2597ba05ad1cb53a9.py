def alinear_secuencias(adn1, adn2):
    alineacion = ""
    i = 0
    j = 0

    while i < len(adn1) and j < len(adn2):
        if adn1[i] == adn2[j]:
            alineacion += adn2[j]
            i += 1
            j += 1
        else:
            alineacion += "_"
            j += 1

    if j < len(adn2):
        alineacion += adn2[j:]

    return alineacion


# Entrada de valores
adn1 = input("Ingrese la primera secuencia de ADN: ")
adn2 = input("Ingrese la segunda secuencia de ADN: ")

# Llamada a la función
alineacion_resultante = alinear_secuencias(adn1, adn2)

# Impresión del resultado
print(alineacion_resultante)

