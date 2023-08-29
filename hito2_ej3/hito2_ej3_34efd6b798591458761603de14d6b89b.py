def encontrar_substrings_unicos(secuencia, n):
    substring_count = {}
    unique_substrings = []

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i + n]
        if substring in substring_count:
            substring_count[substring] += 1
        else:
            substring_count[substring] = 1

    for substring, count in substring_count.items():
        if count == 1:
            unique_substrings.append(substring)

    return unique_substrings

# Pedir al usuario que ingrese la secuencia y el valor de n
secuencia = input("Ingrese la secuencia: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n
substrings_unicos = encontrar_substrings_unicos(secuencia, n)

# Mostrar los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
    