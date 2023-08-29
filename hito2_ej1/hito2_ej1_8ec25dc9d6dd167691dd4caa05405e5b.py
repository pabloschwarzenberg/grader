def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    i = 0
    for base1 in secuencia1:
        if i >= len(secuencia2) or base1 != secuencia2[i]:
            alineacion += "_"
        else:
            alineacion += secuencia2[i]
            i += 1

    if i < len(secuencia2):
        alineacion += secuencia2[i:]

    return alineacion

secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

resultado = alinear_secuencias(secuencia1, secuencia2)

print(resultado)
