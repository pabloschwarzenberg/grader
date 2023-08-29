def align_sequences(seq1, seq2):
    aligned_seq = ""
    index_seq2 = 0

    for char in seq1:
        if char == seq2[index_seq2]:
            aligned_seq += char
            index_seq2 += 1
        else:
            aligned_seq += "_"

    aligned_seq += seq2[index_seq2:]
    return aligned_seq

# Obtener las secuencias de ADN como entrada del usuario
sequence1 = input("Ingrese la primera secuencia de ADN: ")
sequence2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
aligned_sequence = align_sequences(sequence1, sequence2)

# Imprimir el resultado
print(aligned_sequence)
