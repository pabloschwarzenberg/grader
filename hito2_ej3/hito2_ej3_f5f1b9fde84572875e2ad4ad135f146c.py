def encontrar_substrings_unicos(s, n):
    substrings = set()
    unique_substrings = set()

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)

    return unique_substrings

cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = encontrar_substrings_unicos(cadena, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      