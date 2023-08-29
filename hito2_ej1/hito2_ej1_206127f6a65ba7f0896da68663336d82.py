      def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    index2 = 0

    # Recorrer la secuencia1 y agregar "_" en la secuencia2 para alinearlas
    for char1 in secuencia1:
        if char1 == secuencia2[index2]:
            alineacion += char1
            index2 += 1
        else:
            alineacion += "_"
    
    # Agregar los caracteres restantes de la secuencia2
    alineacion += secuencia2[index2:]

    return alineacion


if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    alineacion = alinear_secuencias(secuencia1, secuencia2)
    print(alineacion)
