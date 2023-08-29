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

# Obtener las secuencias de ADN desde la entrada del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print("Resultado del alineamiento:")
print(secuencia_alineada)