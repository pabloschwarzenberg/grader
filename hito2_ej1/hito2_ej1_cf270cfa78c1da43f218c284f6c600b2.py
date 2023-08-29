def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice1 = 0
    indice2 = 0

    # Realizar el alineamiento comparando los caracteres de ambas secuencias
    while indice1 < len(secuencia1) and indice2 < len(secuencia2):
        if secuencia1[indice1] == secuencia2[indice2]:
            alineacion += secuencia2[indice2]
            indice1 += 1
            indice2 += 1
        else:
            alineacion += "_"
            indice2 += 1

    # Completar con '_' los caracteres restantes de la segunda secuencia
    if indice2 < len(secuencia2):
        alineacion += "_" * (len(secuencia2) - indice2)

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingresa la primera secuencia: ")
    secuencia2 = input("Ingresa la segunda secuencia: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)

    print(resultado)
