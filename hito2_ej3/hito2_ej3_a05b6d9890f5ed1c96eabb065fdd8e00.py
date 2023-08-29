def obtener_substrings_unicos(s, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de largo n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]

        # Contar la aparición de cada substring
        contador[substring] = contador.get(substring, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    for substring, count in contador.items():
        if count == 1:
            substrings.append(substring)

    return substrings


if __name__ == "__main__":
    # Leer el string y el entero n
    entrada = input("Ingrese el string y el valor de n separados por espacio: ")
    s, n = entrada.split()
    n = int(n)

    # Convertir el string a mayúsculas
    s = s.upper()

    # Obtener los substrings únicos de largo n
    substrings = obtener_substrings_unicos(s, n)

    # Imprimir los resultados
    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")