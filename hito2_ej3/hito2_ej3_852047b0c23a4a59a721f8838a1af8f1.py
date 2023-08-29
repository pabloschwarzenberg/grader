def obtener_substrings_unicos(secuencia, n):
    substrings = {}

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    return substrings_unicos


# Solicitar al usuario la secuencia y el valor de n
secuencia_input = input("Ingrese la secuencia: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos
substrings_unicos = obtener_substrings_unicos(secuencia_input, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")      