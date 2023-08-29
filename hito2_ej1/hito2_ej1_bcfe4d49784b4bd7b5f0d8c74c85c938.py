def align_sequences(sequence1, sequence2):
    aligned_sequence2 = ""
    i = 0
    for letter in sequence1:
        if i < len(sequence2):
            if letter == sequence2[i]:
                aligned_sequence2 += letter
            else:
                aligned_sequence2 += "_"
            i += 1
        else:
            aligned_sequence2 += "_"
    return aligned_sequence2

sequence1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
sequence2 = "TGACGTTCAGTAGTCGATT"

aligned_sequence2 = align_sequences(sequence1, sequence2)

print('___TG_______A__C_G__TT_C_AGTAGTCGATT')