      def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    index_secuencia2 = 0

    for char in secuencia1:
        if char == secuencia2[index_secuencia2]:
            secuencia_alineada += char
            index_secuencia2 += 1
        else:
            secuencia_alineada += "_"

    secuencia_alineada += secuencia2[index_secuencia2:]

    return secuencia_alineada


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
    print("Secuencia alineada:")
    print(secuencia_alineada)
