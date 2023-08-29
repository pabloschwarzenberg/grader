def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""

    # Iterar sobre cada caracter de la primera secuencia
    for i in range(len(secuencia1)):
        if i < len(secuencia2):
            if secuencia1[i] == secuencia2[i]:
                secuencia_alineada += secuencia2[i]
            else:
                secuencia_alineada += "_"
        else:
            secuencia_alineada += "_"

    return secuencia_alineada

# Obtener las dos secuencias de ADN desde el usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Alinear las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir la secuencia alineada
print(secuencia_alineada)