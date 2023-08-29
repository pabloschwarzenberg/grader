def encontrar_substrings_unicos(cadena, n):
    substrings_contados = {}
    resultado = []

    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings_contados:
            substrings_contados[substring] += 1
        else:
            substrings_contados[substring] = 1

    for substring, count in substrings_contados.items():
        if count == 1:
            resultado.append(substring)

    return resultado

# Ejemplo de uso
cadena_input = input("Ingrese la cadena de texto: ")
n_input = int(input("Ingrese el tamaño de los substrings: "))

substrings_unicos = encontrar_substrings_unicos(cadena_input, n_input)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
