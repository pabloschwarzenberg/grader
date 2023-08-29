 def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    i = 0
    j = 0

    while i < len(secuencia1):
        if j >= len(secuencia2):
            alineacion += "_"
        elif secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            j += 1
        else:
            alineacion += "_"
        i += 1

    if j < len(secuencia2):
        alineacion += secuencia2[j:]

    return alineacion


# Solicitar al usuario que ingrese las secuencias
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de las secuencias
resultado = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(resultado)
