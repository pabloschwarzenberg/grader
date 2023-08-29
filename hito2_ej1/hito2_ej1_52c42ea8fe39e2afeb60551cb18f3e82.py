def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0

    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            secuencia_alineada += caracter
            indice_secuencia2 += 1
        else:
            secuencia_alineada += "_"
    
    secuencia_alineada += secuencia2[indice_secuencia2:]
    return secuencia_alineada

# Entrada de las secuencias
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Llamada a la función de alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Impresión del resultado
print(secuencia_alineada)
