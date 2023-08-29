def find_unique_substrings(s, n):
    substrings = set()
    unique_substrings = set()

    # Generar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.add(substring)

    # Encontrar los substrings únicos
    for substring in substrings:
        if s.count(substring) == 1:
            unique_substrings.add(substring)

    return unique_substrings

# Solicitar la entrada al usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Encontrar los substrings únicos de longitud n
unique_substrings = find_unique_substrings(s, n)

# Imprimir los resultados
if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")

