def encontrar_substrings_unicos(cadena, n):
    substrings = set()
    substrings_repetidos = set()
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            substrings_repetidos.add(substring)
        else:
            substrings.add(substring)
    substrings_unicos = substrings - substrings_repetidos
    return substrings_unicos
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))
substrings_unicos = encontrar_substrings_unicos(cadena, n)
if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")