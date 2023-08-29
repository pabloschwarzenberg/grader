def find_unique_substrings(string, n):
    substr_counts = {}
    unique_substrings = []

    # Iterar sobre todos los substrings de longitud n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]

        # Incrementar el contador del substring actual
        if substring in substr_counts:
            substr_counts[substring] += 1
        else:
            substr_counts[substring] = 1

    # Encontrar los substrings únicos
    for substring, count in substr_counts.items():
        if count == 1:
            unique_substrings.append(substring)

    return unique_substrings

# Obtener la entrada del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Calcular los substrings únicos de longitud n
unique_substrings = find_unique_substrings(string, n)

# Imprimir los resultados
if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
