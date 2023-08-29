def find_unique_substrings(s, n):
    substrings = []
    unique_substrings = []

    # Generar todas las subcadenas de tamaño n
    for i in range(len(s) - n + 1):
        substrings.append(s[i:i+n])

    # Encontrar las subcadenas únicas
    for substring in substrings:
        if substrings.count(substring) == 1:
            unique_substrings.append(substring)

    return unique_substrings


# Obtener la entrada del usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subcadenas únicas
unique_substrings = find_unique_substrings(s, n)

# Imprimir el resultado
if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
