 seq1 = Seq("TGTGACTA") 
seq2 = Seq("CATGGTCA") 
  
aligner = Align.PairwiseAligner() 
  
print(aligner) 
  
alignments = aligner.align(seq1, seq2) 
  
for alignment in alignments: 
    print(alignment)     