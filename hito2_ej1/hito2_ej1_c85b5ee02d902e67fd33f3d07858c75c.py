def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice2 = 0

    for caracter1 in secuencia1:
        if caracter1 == secuencia2[indice2]:
            alineacion += caracter1
            indice2 += 1
        else:
            alineacion += "_"

    alineacion += secuencia2[indice2:].replace("", "_")[1:]

    return alineacion

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)
    print(resultado)
     