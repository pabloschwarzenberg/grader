def encontrar_substrings_unicos(s, n):
    substrings = set()
    count = {}

    
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.add(substring)
        count[substring] = count.get(substring, 0) + 1

    
    encontrados = False
    for substring in substrings:
        if count[substring] == 1:
            print(substring)
            encontrados = True

    if not encontrados:
        print("ninguna")



encontrar_substrings_unicos("ACGACG", 3)
encontrar_substrings_unicos("ACGACGAC", 3)
encontrar_substrings_unicos("AAAAA", 3)
