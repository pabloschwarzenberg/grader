def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    index_secuencia2 = 0

    # Iterar sobre la primera secuencia
    for char1 in secuencia1:
        # Verificar si ya se recorrió toda la segunda secuencia
        if index_secuencia2 >= len(secuencia2):
            alineacion += "_"
        else:
            char2 = secuencia2[index_secuencia2]
            # Verificar si los caracteres son iguales
            if char1 == char2:
                alineacion += char2
                index_secuencia2 += 1
            else:
                alineacion += "_"

    # Agregar los caracteres restantes de la segunda secuencia
    if index_secuencia2 < len(secuencia2):
        alineacion += secuencia2[index_secuencia2:]

    return alineacion


# Obtener las secuencias de ADN desde el usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(alineacion)

