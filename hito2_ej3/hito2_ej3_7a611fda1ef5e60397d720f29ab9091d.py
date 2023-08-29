def find_unique_substrings(s, n):
    unique_substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if s.count(substring) == 1:
            unique_substrings.append(substring)

    if len(unique_substrings) == 0:
        print("ninguna")
    else:
        for substring in unique_substrings:
            print(substring)

# Ejemplos de uso
find_unique_substrings("ACGACG", 3)
find_unique_substrings("ACGACGAC", 3)
find_unique_substrings("AAAAA", 3)

