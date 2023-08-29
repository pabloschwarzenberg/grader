def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    j = 0

    # Recorrer la primera secuencia y alinear la segunda secuencia
    for i in range(len(seq1)):
        if seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            j += 1
        else:
            aligned_seq2 += "_"

    # Alinear los caracteres restantes de la segunda secuencia
    while j < len(seq2):
        aligned_seq2 += seq2[j]
        j += 1

    return aligned_seq2

# Obtener las secuencias de ADN del usuario
seq1 = input("Ingresa la primera secuencia de ADN: ")
seq2 = input("Ingresa la segunda secuencia de ADN: ")

# Obtener la secuencia alineada
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir la secuencia alineada
print(aligned_seq2)