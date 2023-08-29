 def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""

    i = 0
    for nucleotido in secuencia1:
        if nucleotido == secuencia2[i]:
            alineacion += nucleotido
            i += 1
        else:
            alineacion += "_"

    alineacion += secuencia2[i:].replace("", "_")[1:]

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingresa la primera secuencia: ")
    secuencia2 = input("Ingresa la segunda secuencia: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)

    print(resultado)
     