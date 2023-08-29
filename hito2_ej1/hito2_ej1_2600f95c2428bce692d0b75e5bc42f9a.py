def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ''
    indice2 = 0

    for caracter in secuencia1:
        if caracter == secuencia2[indice2]:
            alineacion += caracter
            indice2 += 1
        else:
            alineacion += '_'

    alineacion += secuencia2[indice2:].replace('', '_')

    return alineacion

# Obtener las secuencias desde el usuario
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento de las secuencias
resultado = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print(resultado)
