def alinear_secuencias(seq1, seq2):
    aligned_seq2 = ""
    i = 0
    for base in seq1:
        if base == seq2[i]:
            aligned_seq2 += seq2[i]
            i += 1
        else:
            aligned_seq2 += "_"
    aligned_seq2 += seq2[i:]
    return aligned_seq2

seq1 ="ACCTGGTTCTGTAGTCAGGATTACTA"
seq2 ="TGACGTTCAGTAGTCGATT"
print(alinear_secuencias(seq1,seq2))



