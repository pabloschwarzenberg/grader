def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0

    # Recorrer la secuencia1 y alinearla con la secuencia2
    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            alineacion += caracter
            indice_secuencia2 += 1
        else:
            alineacion += "_"

    # Completar el resto de la secuencia2 si es más larga que la secuencia1
    if indice_secuencia2 < len(secuencia2):
        alineacion += secuencia2[indice_secuencia2:]

    return alineacion

# Obtener las secuencias de ADN desde el usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de las secuencias
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(alineacion)
