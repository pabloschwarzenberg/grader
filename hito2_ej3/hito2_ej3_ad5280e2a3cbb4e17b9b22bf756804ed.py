def encontrar_substrings(s, n):
    substrings = []
    count = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring not in count:
            count[substring] = 1
        else:
            count[substring] += 1
    for substring, frequency in count.items():
        if frequency == 1:
            substrings.append(substring)
    return substrings


cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))


substrings = encontrar_substrings(cadena, n)


if len(substrings) == 0:
    print("ninguna")
else:
    for substring in substrings:
        print(substring)      