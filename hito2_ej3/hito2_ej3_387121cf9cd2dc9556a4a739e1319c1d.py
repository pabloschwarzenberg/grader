def obtener_substrings_unicos(secuencia, n):
    substrings = []
    contador = {}

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        substrings.append(substring)

    for substring in substrings:
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    substrings_unicos = [substring for substring, count in contador.items() if count == 1]

    return substrings_unicos

secuencia_input = input("Ingrese la secuencia: ")
n_input = int(input("Ingrese el valor de N: "))

substrings_unicos = obtener_substrings_unicos(secuencia_input, n_input)

if len(substrings_unicos) == 0:
    print("Ninguna")
else:
    for substring in substrings_unicos:
        print(substring)