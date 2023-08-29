def count_substrings(s, n):
    substr_counts = {}
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if substr in substr_counts:
            substr_counts[substr] += 1
        else:
            substr_counts[substr] = 1
    return substr_counts

def find_unique_substrings(s, n):
    substr_counts = count_substrings(s, n)
    unique_substrings = []
    for substr, count in substr_counts.items():
        if count == 1:
            unique_substrings.append(substr)
    return unique_substrings

# Obtener la entrada del usuario
s = input("Ingresa el string: ")
n = int(input("Ingresa el entero n: "))

# Encontrar los substrings únicos de longitud n
unique_substrings = find_unique_substrings(s, n)

# Imprimir los resultados
if len(unique_substrings) == 0:
    print("ninguna")
else:
    for substr in unique_substrings:
        print(substr)