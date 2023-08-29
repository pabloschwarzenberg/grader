    def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    index_secuencia2 = 0

    for char1 in secuencia1:
        if index_secuencia2 < len(secuencia2) and char1 != secuencia2[index_secuencia2]:
            secuencia_alineada += "_"
        else:
            secuencia_alineada += char1
            index_secuencia2 += 1

    # Alinear el resto de la secuencia2 (si es más larga que la secuencia1)
    if index_secuencia2 < len(secuencia2):
        secuencia_alineada += "_" * (len(secuencia2) - index_secuencia2)

    return secuencia_alineada


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    print(secuencia_alineada)
  