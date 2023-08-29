def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0

    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            alineacion += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            alineacion += "_"

    alineacion += secuencia2[indice_secuencia2:]

    return alineacion
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")
resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)
     