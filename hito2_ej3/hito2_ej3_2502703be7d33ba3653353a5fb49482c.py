def unique_substrings(s, n):
    substrings = set()
    unique_substrings = set()

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)

    return unique_substrings

# Obtener la entrada del usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Obtener los substrings únicos de longitud n
result = unique_substrings(s, n)

# Imprimir los resultados
if len(result) > 0:
    for substring in result:
        print(substring)
else:
    print("ninguna")
      