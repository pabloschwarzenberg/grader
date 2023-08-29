def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    i = 0
    j = 0

    while i < len(secuencia1) and j < len(secuencia2):
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            i += 1
            j += 1
        else:
            alineacion += "_"
            j += 1

    if j < len(secuencia2):
        alineacion += secuencia2[j:]

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    alineacion = alinear_secuencias(secuencia1, secuencia2)
    print(alineacion)
     