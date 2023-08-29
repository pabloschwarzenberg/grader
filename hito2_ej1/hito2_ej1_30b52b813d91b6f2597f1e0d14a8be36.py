def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""

    # Alinear secuencia2 con secuencia1
    index_secuencia2 = 0
    for char1 in secuencia1:
        if index_secuencia2 < len(secuencia2) and char1 == secuencia2[index_secuencia2]:
            alineacion += char1
            index_secuencia2 += 1
        else:
            alineacion += "_"

    # Agregar los caracteres restantes de la secuencia2
    alineacion += secuencia2[index_secuencia2:]

    return alineacion


# Obtener las dos secuencias desde la entrada del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Obtener la alineación de la segunda secuencia con la primera
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir la alineación
print(alineacion)
      