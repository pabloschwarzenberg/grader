def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    i = 0
    j = 0

    # Iterar sobre las secuencias y alinearlas
    while i < len(seq1) and j < len(seq2):
        if seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            i += 1
            j += 1
        else:
            aligned_seq2 += "_"
            i += 1

    # Agregar los caracteres restantes de seq2 si hay alguna diferencia en las longitudes
    if j < len(seq2):
        aligned_seq2 += seq2[j:]

    return aligned_seq2

# Obtener las secuencias de ADN desde la entrada del usuario
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
aligned_seq2 = align_sequences(seq1, seq2)

# Imprimir el resultado del alineamiento
print(aligned_seq2)