def encontrar_substrings_unicos(cadena, n):
    substrings = set()
    substrings_repetidos = set()

    # Obtener todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            substrings_repetidos.add(substring)
        else:
            substrings.add(substring)

    # Encontrar los substrings únicos
    substrings_unicos = substrings - substrings_repetidos

    return substrings_unicos

# Obtener la cadena y el valor de n del usuario
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos
substrings_unicos = encontrar_substrings_unicos(cadena, n)

# Imprimir los substrings únicos o el mensaje "ninguna"
if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
