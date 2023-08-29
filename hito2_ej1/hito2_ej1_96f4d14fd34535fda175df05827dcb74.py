def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    i = 0

    for char in seq1:
        if char == seq2[i]:
            aligned_seq2 += seq2[i]
            i += 1
        else:
            aligned_seq2 += "_"

    return aligned_seq2


# Obtener las secuencias de ADN desde la entrada del usuario
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir el resultado
print(["_" * i + aligned_seq2 for i in range(len(aligned_seq2))])
