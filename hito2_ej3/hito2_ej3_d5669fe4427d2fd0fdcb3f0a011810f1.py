def obtener_substrings_unicos(s, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de largo n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.append(substring)
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]

    return substrings_unicos


# Obtener la entrada del usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Obtener los substrings únicos de largo n
substrings_unicos = obtener_substrings_unicos(s, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      