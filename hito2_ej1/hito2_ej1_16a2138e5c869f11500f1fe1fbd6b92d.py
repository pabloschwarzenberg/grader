def alinear_secuencias(secuencia1, secuencia2):
    alineada = ""
    i = 0
    for c in secuencia1:
        if c == secuencia2[i]:
            alineada += c
            i += 1
        else:
            alineada += "_"
    alineada += secuencia2[i:].replace("", "_")[1:-1]
    return alineada

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    print(secuencia_alineada)
      