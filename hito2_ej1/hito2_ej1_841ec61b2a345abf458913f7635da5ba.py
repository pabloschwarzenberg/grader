def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    i = 0
    for char in seq1:
        if char == seq2[i]:
            aligned_seq2 += seq2[i]
            i += 1
        else:
            aligned_seq2 += "_"
    
    if i < len(seq2):
        aligned_seq2 += seq2[i:]
    
    return aligned_seq2


# Ejemplo de uso
seq1 = input("Ingresa la primera secuencia de ADN: ")
seq2 = input("Ingresa la segunda secuencia de ADN: ")

aligned_seq2 = align_sequences(seq1, seq2)

print(aligned_seq2)
     