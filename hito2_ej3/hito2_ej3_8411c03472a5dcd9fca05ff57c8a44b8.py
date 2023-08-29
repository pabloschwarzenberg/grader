def obtener_substrings_unicos(string, n):
    substrings = []
    counts = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        substrings.append(substring)

    # Contar la frecuencia de cada substring
    for substring in substrings:
        counts[substring] = counts.get(substring, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    unicos = [substring for substring, count in counts.items() if count == 1]

    return unicos

# Solicitar al usuario que ingrese el string y el valor de n
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(string, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
    