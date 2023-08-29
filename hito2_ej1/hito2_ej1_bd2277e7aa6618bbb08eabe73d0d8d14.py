def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ''
    i = 0

    for c in secuencia1:
        if i < len(secuencia2) and c == secuencia2[i]:
            alineacion += secuencia2[i]
            i += 1
        else:
            alineacion += '_'

    if i < len(secuencia2):
        alineacion += secuencia2[i:]

    return alineacion

secuencia1 = input("Introduce la primera secuencia: ")
secuencia2 = input("Introduce la segunda secuencia: ")

resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)