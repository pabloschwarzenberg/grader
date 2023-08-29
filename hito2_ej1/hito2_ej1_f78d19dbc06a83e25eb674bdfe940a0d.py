def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0

    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            alineacion += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            alineacion += "_"

    alineacion += secuencia2[indice_secuencia2:]

    return alineacion


# Obtener las secuencias de ADN desde el usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
resultado = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(resultado)
