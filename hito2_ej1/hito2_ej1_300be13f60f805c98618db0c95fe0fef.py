def align_sequences(seq1, seq2):
    aligned_seq = ""
    index_seq2 = 0

    for char in seq1:
        if index_seq2 < len(seq2) and char == seq2[index_seq2]:
            aligned_seq += seq2[index_seq2]
            index_seq2 += 1
        else:
            aligned_seq += "_"

    if index_seq2 < len(seq2):
        aligned_seq += seq2[index_seq2:]

    return aligned_seq


# Obtener las secuencias de ADN como entrada
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar la alineación de las secuencias
aligned_sequence = align_sequences(seq1, seq2)

# Imprimir el resultado de la alineación
print("Secuencia alineada:")
print(aligned_sequence)
