def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ''
    index_secuencia2 = 0

    for caracter in secuencia1:
        if index_secuencia2 < len(secuencia2) and caracter == secuencia2[index_secuencia2]:
            secuencia_alineada += caracter
            index_secuencia2 += 1
        else:
            secuencia_alineada += '_'

    secuencia_alineada += secuencia2[index_secuencia2:].replace('', '_')[1:-1]

    return secuencia_alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    print("Secuencia alineada:")
    print(secuencia_alineada)
