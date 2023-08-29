def obtener_substrings_unicos(s, n):
    substrings_unicos = set()
    substrings_duplicados = set()

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings_unicos:
            substrings_duplicados.add(substring)
        else:
            substrings_unicos.add(substring)

    substrings_unicos -= substrings_duplicados

    return list(substrings_unicos)

s = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = obtener_substrings_unicos(s, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
