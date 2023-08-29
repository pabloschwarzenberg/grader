def encontrar_substrings_unicos(cadena, n):
    substrings = set()
    unicos = set()

    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            unicos.discard(substring)
        else:
            substrings.add(substring)
            unicos.add(substring)

    return unicos

# Solicitar la cadena y el valor de n al usuario
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n
substrings_unicos = encontrar_substrings_unicos(cadena, n)

# Mostrar los substrings únicos encontrados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")