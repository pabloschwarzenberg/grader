def obtener_substrings_unicos(string, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        substrings.append(substr)
        contador[substr] = contador.get(substr, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    resultados = [substr for substr in substrings if contador[substr] == 1]

    return resultados


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))

    resultados = obtener_substrings_unicos(string, n)

    if len(resultados) > 0:
        for resultado in resultados:
            print(resultado)
    else:
        print("ninguna")

    