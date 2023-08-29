def encontrar_substrings_unicos(cadena, n):
    substrings = set()
    contador = {}

    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]

        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    for substring, count in contador.items():
        if count == 1:
            substrings.add(substring)

    return substrings


if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))

    resultados = encontrar_substrings_unicos(cadena, n)

    if len(resultados) > 0:
        for substring in resultados:
            print(substring)
    else:
        print("ninguna")      