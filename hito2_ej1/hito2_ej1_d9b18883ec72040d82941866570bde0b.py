def alinear_secuencias(seq1, seq2):
    aligned_seq2 = ""
    i = 0
    for base in seq1:
        if i < len(seq2):
            if base == seq2[i]:
                aligned_seq2 += seq2[i]
                i += 1
            else:
                aligned_seq2 += "_"
        else:
            aligned_seq2 += "_"
    aligned_seq2 += seq2[i:]
    return aligned_seq2

seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinear_secuencias(seq1, seq2)
print("Secuencia alineada:", resultado)
