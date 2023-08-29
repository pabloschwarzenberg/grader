def encontrar_substrings_unicos(secuencia, n):
    substrings = set()
    repetidos = set()

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            repetidos.add(substring)
        else:
            substrings.add(substring)

    substrings_unicos = substrings - repetidos
    return substrings_unicos

# Obtener la secuencia y el valor de n desde el usuario
secuencia = input("Ingrese la secuencia: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n
substrings_unicos = encontrar_substrings_unicos(secuencia, n)

# Imprimir los substrings únicos
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      