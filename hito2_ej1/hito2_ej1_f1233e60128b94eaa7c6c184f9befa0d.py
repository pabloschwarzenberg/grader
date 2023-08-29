def alinear_secuencias(seq1, seq2):
    aligned_seq2 = ""
    j = 0

    for i in range(len(seq1)):
        if j < len(seq2) and seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            j += 1
        else:
            aligned_seq2 += "_"

    return aligned_seq2

if __name__ == "__main__":
    seq1 = input("Ingrese la primera secuencia de ADN: ")
    seq2 = input("Ingrese la segunda secuencia de ADN: ")

    aligned_seq2 = alinear_secuencias(seq1, seq2)
    print(aligned_seq2)
      