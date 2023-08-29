def encontrar_substrings_unicos(string, n):
    substrings = []
    counts = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        substrings.append(substring)

    # Contar la aparición de cada substring
    for substring in substrings:
        if substring in counts:
            counts[substring] += 1
        else:
            counts[substring] = 1

    # Filtrar los substrings únicos
    unique_substrings = [substring for substring, count in counts.items() if count == 1]

    return unique_substrings

# Obtener el string y el valor de n del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n
substrings_unicos = encontrar_substrings_unicos(string, n)

# Imprimir los substrings únicos encontrados o el mensaje "ninguna"
if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      