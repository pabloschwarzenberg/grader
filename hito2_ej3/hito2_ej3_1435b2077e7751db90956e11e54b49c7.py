def obtener_substrings_unicos(string, n):
    substrings = set()
    resultados = []

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring not in substrings and string.count(substring) == 1:
            substrings.add(substring)
            resultados.append(substring)

    return resultados


if __name__ == "__main__":
    entrada = input("Ingrese el string y el valor de n separados por espacio: ")
    elementos = entrada.split()
    string = elementos[0]
    n = int(elementos[1])

    substrings_unicos = obtener_substrings_unicos(string, n)

    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
