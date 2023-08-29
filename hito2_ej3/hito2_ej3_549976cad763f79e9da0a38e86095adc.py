def obtener_substrings_unicos(secuencia, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de largo n
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        substrings.append(substring)
        if substring not in contador:
            contador[substring] = 1
        else:
            contador[substring] += 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]

    return substrings_unicos


# Pedir la entrada al usuario
secuencia_input = input("Ingrese la secuencia: ")
n_input = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos
substrings_unicos = obtener_substrings_unicos(secuencia_input, n_input)

# Imprimir los resultados
if len(substrings_unicos) == 0:
    print("ninguna")
else:
    for substring in substrings_unicos:
        print(substring)
