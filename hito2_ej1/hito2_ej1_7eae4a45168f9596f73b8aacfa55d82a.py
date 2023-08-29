def alinear_strings(secuencia1, secuencia2):
    # Inicializamos algunas variables importantes
    alineamiento = ""
    indice2 = 0

    # Recorremos la primera secuencia
    for caracter in secuencia1:
        # Si el caracter actual coincide con el siguiente de la segunda secuencia, lo agregamos a la salida
        if caracter == secuencia2[indice2]:
            alineamiento += caracter
            indice2 += 1
        # Si no, agregamos un guión bajo
        else:
            alineamiento += "_"

    # Agregamos los caracteres restantes de la segunda secuencia (si hay alguno)
    if indice2 < len(secuencia2):
        alineamiento += secuencia2[indice2:]

    return alineamiento

# Pedimos las entradas al usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Llamamos a la función y mostramos la salida
print(alinear_strings(secuencia1, secuencia2))