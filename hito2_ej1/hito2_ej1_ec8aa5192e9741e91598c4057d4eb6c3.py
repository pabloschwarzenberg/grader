def align_sequences(seq1, seq2):
    aligned_seq2 = ""

    i = 0
    j = 0

    while i < len(seq1):
        if j >= len(seq2):
            aligned_seq2 += "_"
            i += 1
        elif seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            i += 1
            j += 1
        else:
            aligned_seq2 += "_"
            i += 1

    if j < len(seq2):
        aligned_seq2 += seq2[j:]

    return aligned_seq2

# Entrada de datos
seq1 = input("Ingrese la primera secuencia: ")
seq2 = input("Ingrese la segunda secuencia: ")

# Llamada a la función
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir resultado
print(aligned_seq2)
