def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0

    for caracter in secuencia1:
        if caracter == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += "_"

    secuencia_alineada += secuencia2[i:]
    return secuencia_alineada


# Lectura de las secuencias desde la entrada estándar
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(secuencia_alineada)