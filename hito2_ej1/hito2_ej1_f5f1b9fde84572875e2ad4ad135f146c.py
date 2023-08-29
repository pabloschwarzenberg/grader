def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0
    for letra in secuencia1:
        if indice_secuencia2 < len(secuencia2):
            if letra == secuencia2[indice_secuencia2]:
                secuencia_alineada += letra
                indice_secuencia2 += 1
            else:
                secuencia_alineada += "_"
        else:
            secuencia_alineada += "_"
    secuencia_alineada += secuencia2[indice_secuencia2:].rjust(len(secuencia1) - len(secuencia_alineada), "_")
    return secuencia_alineada

# Obtener las secuencias de ADN del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento de las secuencias
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(secuencia_alineada)
