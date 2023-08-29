def obtener_substrings_unicos(s, n):
    substrings = []

    # Obtener todos los substrings de longitud n de la cadena s
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        substrings.append(substring)

    # Contar la frecuencia de cada substring
    frecuencias = {}
    for substring in substrings:
        if substring in frecuencias:
            frecuencias[substring] += 1
        else:
            frecuencias[substring] = 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = []
    for substring in frecuencias:
        if frecuencias[substring] == 1:
            substrings_unicos.append(substring)

    return substrings_unicos

# Solicitar al usuario que ingrese la cadena y el valor de n
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(cadena, n)

# Imprimir los substrings únicos o "ninguna" si no hay ninguno
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")