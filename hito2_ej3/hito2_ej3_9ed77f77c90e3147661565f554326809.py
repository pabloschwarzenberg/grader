def obtener_substrings_unicos(cadena, n):
    substrings = {}
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    substrings_unicos = []
    for substring, count in substrings.items():
        if count == 1:
            substrings_unicos.append(substring)

    return substrings_unicos


# Solicitar la cadena y el valor de n al usuario
cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings = obtener_substrings_unicos(cadena, n)

# Imprimir los resultados
if len(substrings) > 0:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")
