def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia1 = 0
    
    for caracter in secuencia2:
        if indice_secuencia1 < len(secuencia1) and caracter == secuencia1[indice_secuencia1]:
            secuencia_alineada += caracter
            indice_secuencia1 += 1
        else:
            secuencia_alineada += "_"
    
    return secuencia_alineada

# Obtener la entrada del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Alinear las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(secuencia_alineada)