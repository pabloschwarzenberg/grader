def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    j = 0

    for i in range(len(seq1)):
        if j < len(seq2) and seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            j += 1
        else:
            aligned_seq2 += "_"

    return [aligned_seq2]

# Obtener las secuencias de ADN desde el usuario
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir el resultado
print(aligned_seq2)
