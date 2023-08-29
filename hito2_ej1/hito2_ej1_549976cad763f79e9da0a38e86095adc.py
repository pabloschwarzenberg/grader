 def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0

    for nucleotido in secuencia1:
        if nucleotido == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
        else:
            secuencia_alineada += "_"
        i += 1

    secuencia_alineada += secuencia2[i:].replace("", "_")[1:]

    return secuencia_alineada


# Pedir la entrada al usuario
secuencia1_input = input("Ingrese la primera secuencia: ")
secuencia2_input = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1_input, secuencia2_input)

# Imprimir el resultado
print(secuencia_alineada)
