def encontrar_substrings_unicos(cadena, n):
    substrings = {}

    # Generar todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    # Encontrar los substrings únicos
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    return substrings_unicos


# Obtener la cadena y el valor de n del usuario
cadena_input = input("Ingrese una cadena: ")
n_input = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos
substrings_unicos = encontrar_substrings_unicos(cadena_input, n_input)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
