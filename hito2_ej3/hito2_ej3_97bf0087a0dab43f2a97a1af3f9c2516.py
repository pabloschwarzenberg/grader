def encontrar_substrings_unicos(s, n):
    substrings = set()  # Conjunto para almacenar los substrings únicos
    count = {}  # Diccionario para contar la frecuencia de los substrings

    # Generar todos los substrings de longitud n y contar su frecuencia
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        count[substring] = count.get(substring, 0) + 1

    # Agregar los substrings únicos al conjunto
    for substring, frequency in count.items():
        if frequency == 1:
            substrings.add(substring)

    return substrings

# Obtener la cadena y la longitud del usuario
cadena = input("Ingrese la cadena: ")
longitud = int(input("Ingrese la longitud de los substrings: "))

# Encontrar los substrings únicos
substrings_unicos = encontrar_substrings_unicos(cadena, longitud)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")      