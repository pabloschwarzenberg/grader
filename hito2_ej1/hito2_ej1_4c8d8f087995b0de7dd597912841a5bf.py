def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0  # Índice para recorrer la secuencia2

    for nucleotido in secuencia1:
        if nucleotido == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += "_"

    # Agregar los caracteres restantes de secuencia2
    secuencia_alineada += secuencia2[i:]

    return secuencia_alineada


# Solicitar las secuencias al usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)
