def encontrar_substrings_unicos(s, n):
    substrings = []
    count = {}

    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        count[substring] = count.get(substring, 0) + 1

    for substring, freq in count.items():
        if freq == 1:
            substrings.append(substring)

    return substrings


# Entrada de valores
s = input("Ingresa el string: ")
n = int(input("Ingresa el tamaño de los substrings: "))

# Llamada a la función
substrings_unicos = encontrar_substrings_unicos(s, n)

# Impresión de resultados
if len(substrings_unicos) == 0:
    print("ninguna")
else:
    for substring in substrings_unicos:
        print(substring)
