def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ''
    j = 0
    for i in range(len(secuencia1)):
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            j += 1
        else:
            alineacion += '_'
    return alineacion

secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)
