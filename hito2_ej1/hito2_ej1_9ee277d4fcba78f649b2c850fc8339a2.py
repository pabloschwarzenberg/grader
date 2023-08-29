 def align_sequences(seq1, seq2):
    aligned_seq = ""
    i = 0
    for char in seq2:
        if char == seq1[i]:
            aligned_seq += char
            i += 1
        else:
            aligned_seq += "_"

    return aligned_seq

if __name__ == "__main__":
    seq1 = input("Ingrese la primera secuencia de ADN: ")
    seq2 = input("Ingrese la segunda secuencia de ADN: ")

    aligned_seq = align_sequences(seq1, seq2)

    print(aligned_seq)
