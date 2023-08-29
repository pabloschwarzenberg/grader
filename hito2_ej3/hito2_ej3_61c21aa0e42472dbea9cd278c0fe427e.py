def subsecuencia_de_adn(sequence,large):
    l = []
    lf = []
    i = 0
    while (i+large) <= (len(sequence)):
        l += [sequence[i:(i+large)]]
        i += 1
    for subsequence in l:
        if l.count(subsequence) == 1:
            lf += [subsequence]
    if len(lf) == 0:
        return print("ninguna")
    for subsequencef in lf:
        print(subsequencef)

sequence = input()
large = int(input())

subsecuencia_de_adn(sequence,large)