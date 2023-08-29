def obtener_substrings_unicos(cadena, n):
    substrings = []
    contador = {}

    # Generar todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        substrings.append(substring)
        contador[substring] = contador.get(substring, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]

    return substrings_unicos

if __name__ == "__main__":
    cadena = input("Ingrese la cadena de texto: ")
    n = int(input("Ingrese la longitud de los substrings: "))

    substrings_unicos = obtener_substrings_unicos(cadena, n)

    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
