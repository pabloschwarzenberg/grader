def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ''
    indice_secuencia2 = 0

    for caracter in secuencia1:
        if indice_secuencia2 < len(secuencia2) and caracter == secuencia2[indice_secuencia2]:
            alineacion += caracter
            indice_secuencia2 += 1
        else:
            alineacion += '_'

    alineacion += secuencia2[indice_secuencia2:]  # Agregar el resto de la segunda secuencia

    return alineacion

# Obtener las secuencias desde la entrada
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

# Realizar la alineación
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado
print(alineacion)
