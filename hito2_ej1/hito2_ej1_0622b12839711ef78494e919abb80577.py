def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0
    for c in secuencia1:
        if i < len(secuencia2) and c == secuencia2[i]:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += "_"
    secuencia_alineada += secuencia2[i:].replace("", "_")[1:]
    return secuencia_alineada


# Obtener las secuencias de ADN como entrada del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Alinear las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)