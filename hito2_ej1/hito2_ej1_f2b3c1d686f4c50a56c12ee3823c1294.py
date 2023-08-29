def align_sequences(seq1, seq2):
    aligned_seq2 = ""
    j = 0

    for i in range(len(seq1)):
        if j < len(seq2) and seq1[i] == seq2[j]:
            aligned_seq2 += seq2[j]
            j += 1
        else:
            aligned_seq2 += "_"

    aligned_seq2 += seq2[j:]

    return aligned_seq2

sequence1 = input("Ingrese la primera secuencia de ADN: ")
sequence2 = input("Ingrese la segunda secuencia de ADN: ")

aligned_sequence2 = align_sequences(sequence1, sequence2)

print(aligned_sequence2)
