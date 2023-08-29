def imprimir_substrings_unicos(s, n):
    substrings = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]

        # Verificar si el substring ya está en el diccionario
        if substring in substrings:
            substrings[substring] = False
        else:
            substrings[substring] = True

    # Imprimir los substrings únicos
    found = False
    for substring, unique in substrings.items():
        if unique:
            print(substring)
            found = True

    # Imprimir el mensaje si no se encontraron substrings únicos
    if not found:
        print("ninguna")


if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el tamaño de los substrings: "))

    imprimir_substrings_unicos(s, n)
