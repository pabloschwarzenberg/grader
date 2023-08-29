def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""

    i = 0
    j = 0

    while i < len(secuencia1):
        if j >= len(secuencia2) or secuencia1[i] != secuencia2[j]:
            alineacion += "_"
        else:
            alineacion += secuencia2[j]
            j += 1
        i += 1

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)

    print(resultado)
