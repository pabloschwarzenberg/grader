def obtener_substrings_unicos(string, n):
    substrings = {}

    # Obtener todos los substrings de longitud n y contar su frecuencia
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    # Filtrar los substrings únicos
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]

    return substrings_unicos


# Solicitar al usuario que ingrese el string y el valor de n
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(string, n)

# Imprimir los substrings únicos encontrados
if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      