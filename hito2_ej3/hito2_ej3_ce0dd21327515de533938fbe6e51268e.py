def unique_substrings(s, n):
    substrings = []
    count = {}

    # Generar todos los substrings de largo n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.append(substring)
        count[substring] = count.get(substring, 0) + 1

    unique_substrings = []

    # Encontrar los substrings que aparecen una única vez
    for substring in substrings:
        if count[substring] == 1:
            unique_substrings.append(substring)

    return unique_substrings


# Obtener el string y el entero n desde el usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Obtener los substrings únicos de largo n
result = unique_substrings(s, n)

# Imprimir los resultados
if len(result) == 0:
    print("ninguna")
else:
    for substring in result:
        print(substring)
