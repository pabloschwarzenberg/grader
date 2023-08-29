def alinear_secuencias(secuencia1, secuencia2):
    alineada = ""
    i = 0
    for letra in secuencia1:
        if letra == secuencia2[i]:
            alineada += secuencia2[i]
            i += 1
        else:
            alineada += "_"
    alineada += secuencia2[i:]
    return alineada

secuencia1 = input("Introduce la primera secuencia: ")
secuencia2 = input("Introduce la segunda secuencia: ")

resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)