def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    i = 0

    for char in seq1:
        if char == seq2[i]:
            aligned_seq2 += seq2[i]
            i += 1
        else:
            aligned_seq2 += "_"

    aligned_seq2 += seq2[i:]

    return aligned_seq2

# Obtener la entrada del usuario
seq1 = input("Ingresa la primera secuencia de ADN: ")
seq2 = input("Ingresa la segunda secuencia de ADN: ")

# Llamar a la función
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir el resultado
print(aligned_seq2)
