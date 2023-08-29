def align_sequences(seq1, seq2):
    aligned_seq2 = ''
    i = 0

    # Recorrer cada carácter de la primera secuencia
    for char in seq1:
        if char == seq2[i]:
            aligned_seq2 += seq2[i]
            i += 1
        else:
            aligned_seq2 += '_'

    # Agregar los caracteres restantes de la segunda secuencia
    aligned_seq2 += seq2[i:]

    return aligned_seq2


# Obtener la entrada del usuario
seq1 = input("Ingrese la primera secuencia: ")
seq2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir el resultado
print(aligned_seq2)
