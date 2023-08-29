# Pedimos al usuario que ingrese las dos secuencias de ADN
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")
# Convertimos ambas secuencias a listas para poder trabajar con ellas
seq1_list = list(seq1.upper())
seq2_list = list(seq2.upper())
pos = 0
for i in range(len(seq2_list)):
    if seq2_list[i] != seq1_list[pos]:
        seq2_list.insert(i, "_")
    else:
        pos += 1
aligned_seq2 = "".join(seq2_list)
print(aligned_seq2)
   