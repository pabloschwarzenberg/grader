 def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice_secuencia2 = 0

    # Recorrer la secuencia1 y alinearla con secuencia2
    for caracter in secuencia1:
        if caracter == secuencia2[indice_secuencia2]:
            alineacion += caracter
            indice_secuencia2 += 1
        else:
            alineacion += "_"

    # Completar la alineación con el resto de secuencia2
    alineacion += secuencia2[indice_secuencia2:]

    return alineacion

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    resultado = alinear_secuencias(secuencia1, secuencia2)
    print(resultado)
     