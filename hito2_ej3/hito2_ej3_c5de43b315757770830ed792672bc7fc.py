def obtener_substrings_unicos(s, n):
    # Crear un diccionario para contar la frecuencia de cada substring
    substr_count = {}

    # Obtener todos los substrings de longitud n y contar su frecuencia
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substr_count:
            substr_count[substring] += 1
        else:
            substr_count[substring] = 1

    # Filtrar los substrings que aparecen una única vez
    unique_substrings = [substring for substring, count in substr_count.items() if count == 1]

    return unique_substrings

# Obtener la cadena y el valor de n desde el usuario
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(cadena, n)

# Imprimir los substrings únicos encontrados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      