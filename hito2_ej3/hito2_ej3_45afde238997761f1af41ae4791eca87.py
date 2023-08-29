def obtener_substrings_unicos(string, n):
    substrings = set()

    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        substrings.add(substr)

    unique_substrings = []

    # Verificar si los substrings son únicos
    for substr in substrings:
        if string.count(substr) == 1 and len(set(substr)) == n:
            unique_substrings.append(substr)

    return unique_substrings

# Solicitar el string y el valor de n al usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de largo n
resultados = obtener_substrings_unicos(string, n)

# Imprimir los resultados
if len(resultados) == 0:
    print("ninguna")
else:
    print(resultados)
