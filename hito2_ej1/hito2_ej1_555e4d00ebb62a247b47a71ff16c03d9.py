def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ''
    i = 0

    for nucleotido in secuencia1:
        if i < len(secuencia2) and nucleotido == secuencia2[i]:
            alineacion += nucleotido
            i += 1
        else:
            alineacion += '_'

    alineacion += secuencia2[i:].replace('', '_')[1:]

    return [alineacion]

# Solicitar al usuario las dos secuencias de ADN
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
alineacion_resultante = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(alineacion_resultante)
