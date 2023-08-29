def obtener_substrings_unicos(secuencia, n):
    substrings = []
    count = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        substrings.append(substring)

        # Contar la aparición de cada substring
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    # Filtrar los substrings únicos
    substrings_unicos = [substring for substring in substrings if count[substring] == 1]
    return substrings_unicos


# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia: ")

# Obtener el valor de n del usuario
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(secuencia, n)

# Imprimir los substrings únicos
if len(substrings_unicos) == 0:
    print("ninguna")
else:
    for substring in substrings_unicos:
        print(substring)
