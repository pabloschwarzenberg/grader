seq1 = list(input())
seq2 = input()

idx = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[idx]:
        seq1[i] = '_'
    else:
        idx += 1

res = ''.join(seq1) + seq2[idx:]

print(res)     