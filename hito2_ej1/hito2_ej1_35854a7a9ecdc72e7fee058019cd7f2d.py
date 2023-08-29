def alinearSecuencias(secuencia1, secuencia2):
    alineado = ""
    indice_secuencia2 = 0

    for nucleotido in secuencia1:
        if indice_secuencia2 < len(secuencia2) and nucleotido != secuencia2[indice_secuencia2]:
            alineado += "_"
        else:
            alineado += secuencia2[indice_secuencia2] if indice_secuencia2 < len(secuencia2) else "_"
            indice_secuencia2 += 1

    alineado += secuencia2[indice_secuencia2:] if indice_secuencia2 < len(secuencia2) else ""

    return alineado

secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinearSecuencias(secuencia1, secuencia2)
print(resultado)