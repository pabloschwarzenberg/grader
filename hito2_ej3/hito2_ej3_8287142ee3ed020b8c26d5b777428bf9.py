def obtener_substrings_unicos(string, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        substrings.append(substring)

    # Contar la frecuencia de cada substring
    for substring in substrings:
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in contador.items() if count == 1]

    return substrings_unicos

# Obtener el string y el valor de n desde la entrada
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de largo n
substrings_unicos = obtener_substrings_unicos(string, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
