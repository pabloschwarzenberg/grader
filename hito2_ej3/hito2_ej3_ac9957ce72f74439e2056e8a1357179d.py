def substrings(string, n):
    memory = []

    for index, char in enumerate(string):
        new_word = string[index:index + n]
        if len(new_word) == n:
            count = 0
            for idx, chr in enumerate(string):
                if string[idx:idx+n] == new_word:
                    count += 1
            if count == 1:
                memory.append(new_word)

    if len(memory) == 0:
        print("ninguna")
    else:
        for sequence in memory:
            print(sequence)


substrings(input(), int(input()))
