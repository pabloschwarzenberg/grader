def obtener_substrings_unicos(cadena, n):
    substrings = []
    contador = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        substrings.append(substring)

    # Contar la frecuencia de cada substring
    for substring in substrings:
        contador[substring] = contador.get(substring, 0) + 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in contador.items() if count == 1]

    return substrings_unicos

if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))

    substrings = obtener_substrings_unicos(cadena, n)

    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")
      