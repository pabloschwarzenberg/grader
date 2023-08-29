 from Bio import pairwise2

seq1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
seq2 = "TGACGTTCAGTAGTCGATT"

alignments = pairwise2.align.globalxx(seq1, seq2)

aligned_seq2 = alignments[0][1]
aligned_seq2 = aligned_seq2.replace("-", "_")

print(aligned_seq2)     