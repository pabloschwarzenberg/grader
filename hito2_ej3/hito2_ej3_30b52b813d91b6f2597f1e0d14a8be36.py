def obtener_substrings_unicos(string, n):
    substrings = []
    count = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        substrings.append(substring)

    # Contar la frecuencia de cada substring
    for substring in substrings:
        count[substring] = count.get(substring, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring in count if count[substring] == 1]

    return substrings_unicos

# Obtener el string y el entero n desde la entrada del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(string, n)

# Imprimir los substrings únicos
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      