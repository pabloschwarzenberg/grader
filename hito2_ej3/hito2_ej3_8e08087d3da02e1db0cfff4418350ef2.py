def unique_substrings(s, n):
    substrings = set()
    unique_substrings = set()

    # Obtener todos los substrings de largo n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.add(substring)

    # Encontrar los substrings que aparecen una única vez
    for substring in substrings:
        if s.count(substring) == 1:
            unique_substrings.add(substring)

    return unique_substrings

# Obtener la entrada del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Obtener los substrings únicos de largo n
result = unique_substrings(string, n)

# Imprimir los resultados
if len(result) > 0:
    for substring in result:
        print(substring)
else:
    print("ninguna")
      