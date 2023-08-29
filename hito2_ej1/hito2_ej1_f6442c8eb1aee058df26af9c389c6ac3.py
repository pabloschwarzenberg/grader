def alinear_secuencias(secuencia1, secuencia2):
    len1 = len(secuencia1)
    len2 = len(secuencia2)

    idx2 = 0
    alineacion = []

    for char in secuencia1:
        if idx2 < len2:
            if char == secuencia2[idx2]:
                alineacion.append(secuencia2[idx2])
                idx2 += 1
            else:
                alineacion.append("_")
        else:
            alineacion.append("_")

    while idx2 < len2:
        alineacion.append(secuencia2[idx2])
        idx2 += 1

    alineacion_str = "".join(alineacion)

    return alineacion_str


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)

    print("Resultado del alineamiento:")
    print(resultado)