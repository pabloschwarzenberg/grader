def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0

    for base1 in secuencia1:
        if i < len(secuencia2) and base1 == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += "_"
        
    if i < len(secuencia2):
        secuencia_alineada += secuencia2[i:]

    return secuencia_alineada


# Solicitar al usuario las secuencias
secuencia1_input = input("Ingrese la primera secuencia: ")
secuencia2_input = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1_input, secuencia2_input)

# Imprimir el resultado
print(secuencia_alineada)