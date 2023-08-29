def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    i = 0

    for j in range(len(secuencia2)):
        if i < len(secuencia1) and secuencia1[i] == secuencia2[j]:
            secuencia_alineada += secuencia2[j]
            i += 1
        else:
            secuencia_alineada += "_"

    secuencia_alineada += secuencia2[j+1:].replace("", "_")[1:]

    return secuencia_alineada

# Solicitar las secuencias al usuario
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Mostrar el resultado del alineamiento
print(secuencia_alineada)
