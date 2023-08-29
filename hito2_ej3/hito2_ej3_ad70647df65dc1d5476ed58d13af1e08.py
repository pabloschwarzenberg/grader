def find_unique_substrings(string, n):
    substrings = set()
    unique_substrings = set()

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)

    return unique_substrings


# Obtener el string y el valor de n del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de largo n
unique_substrings = find_unique_substrings(string, n)

# Imprimir los resultados
if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
      