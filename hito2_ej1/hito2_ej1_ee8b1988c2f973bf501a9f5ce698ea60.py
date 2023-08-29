def alinear_secuencias(secuencia1, secuencia2):
    aligned_seq2 = ""
    index = 0

    for char in secuencia1:
        if char == secuencia2[index]:
            aligned_seq2 += secuencia2[index]
            index += 1
        else:
            aligned_seq2 += "_"

    # Agregar los caracteres restantes de secuencia2 si es más larga que secuencia1
    aligned_seq2 += secuencia2[index:]

    return aligned_seq2

# Obtener las secuencias de ADN del usuario
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

# Obtener el segundo string alineado con el primero
aligned_seq2 = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el segundo string alineado
print(aligned_seq2)
