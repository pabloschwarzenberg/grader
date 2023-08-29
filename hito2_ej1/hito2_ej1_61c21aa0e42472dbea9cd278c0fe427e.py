def alineamiento_de_secuencias(sequence1, sequence2):
    l = list(sequence1)
    k = 0
    u = 0
    for i in range(0, len(sequence1)):
        if l[i] != sequence2[k]:
            l.pop(i)
            l.insert(i, "_")
        elif l[i] == sequence2[k]:
            k += 1
        if i == (len(sequence1) - 1):
            l.pop(i)
            l.insert(i, sequence2[k-1:])
            print(sequence2[k:])
    return print("".join(l))


sequence1 = input()
sequence2 = input()
alineamiento_de_secuencias(sequence1, sequence2)