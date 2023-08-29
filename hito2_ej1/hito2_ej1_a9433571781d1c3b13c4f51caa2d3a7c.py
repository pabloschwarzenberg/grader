def alinear_secuencias(seq1, seq2):
    aligned_seq = ""

    # Calcular la longitud máxima para el bucle
    max_length = max(len(seq1), len(seq2))

    # Alinear las secuencias agregando caracteres '_' en la segunda secuencia
    for i in range(max_length):
        if i < len(seq1) and i < len(seq2):
            if seq1[i] == seq2[i]:
                aligned_seq += seq2[i]
            else:
                aligned_seq += "_"
        elif i < len(seq2):
            aligned_seq += "_"

    return aligned_seq

# Solicitar las secuencias al usuario
seq1 = input("Ingrese la primera secuencia: ")
seq2 = input("Ingrese la segunda secuencia: ")

# Realizar el alineamiento de las secuencias
aligned_seq = alinear_secuencias(seq1, seq2)

# Imprimir el resultado del alineamiento
print([aligned_seq])