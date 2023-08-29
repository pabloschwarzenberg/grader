def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""

    for letra1, letra2 in zip(secuencia1, secuencia2):
        if letra1 == letra2:
            alineacion += letra2
        else:
            alineacion += "_"

    return alineacion

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    alineacion = alinear_secuencias(secuencia1, secuencia2)

    print([alineacion])
      