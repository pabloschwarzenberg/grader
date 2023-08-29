def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""

    # Obtener la longitud de las secuencias
    len1 = len(secuencia1)
    len2 = len(secuencia2)

    # Inicializar los índices de las secuencias
    i = 0
    j = 0

    # Realizar la alineación
    while i < len1 and j < len2:
        if secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            i += 1
            j += 1
        else:
            alineacion += "_"
            j += 1

    # Completar el resto de la segunda secuencia con _
    while j < len2:
        alineacion += "_"
        j += 1

    return alineacion


if __name__ == "__main__":
    # Solicitar al usuario que ingrese las secuencias de ADN
    secuencia1 = input("Ingrese la primera secuencia de ADN: ")
    secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

    # Obtener la alineación de las secuencias
    alineacion = alinear_secuencias(secuencia1, secuencia2)

    # Imprimir el resultado de la alineación
    print(alineacion)

      