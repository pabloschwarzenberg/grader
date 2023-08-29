def obtener_substrings(cadena, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
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


# Pedir al usuario que ingrese la cadena y el valor de n
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings(cadena, n)

# Imprimir los substrings únicos
if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
