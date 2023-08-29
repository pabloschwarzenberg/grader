def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ''
    indice_secuencia2 = 0

    for base in secuencia1:
        if base == secuencia2[indice_secuencia2]:
            secuencia_alineada += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            secuencia_alineada += '_'

        if indice_secuencia2 == len(secuencia2):
            break

    if indice_secuencia2 < len(secuencia2):
        secuencia_alineada += '_' * (len(secuencia1) - len(secuencia_alineada))
        secuencia_alineada += secuencia2[indice_secuencia2:]

    return secuencia_alineada


# Obtener las secuencias de ADN desde la entrada
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(secuencia_alineada)
