def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0
    j = 0

    # Recorrer las secuencias y realizar el alineamiento
    while i < len(secuencia1):
        if j < len(secuencia2) and secuencia1[i] == secuencia2[j]:
            secuencia_alineada += secuencia2[j]
            j += 1
        else:
            secuencia_alineada += "_"
        i += 1

    # Completar la secuencia alineada con los caracteres restantes de secuencia2
    while j < len(secuencia2):
        secuencia_alineada += secuencia2[j]
        j += 1

    return secuencia_alineada

# Obtener las secuencias del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir la secuencia alineada
print(secuencia_alineada)
