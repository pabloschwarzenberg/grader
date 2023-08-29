def obtener_substrings_unicos(string, n):
    # Crear un diccionario para contar la frecuencia de los substrings
    frecuencia = {}

    # Obtener todos los substrings de largo n y contar su frecuencia
    for i in range(len(string) - n + 1):
        substring = string[i : i + n]
        if substring in frecuencia:
            frecuencia[substring] += 1
        else:
            frecuencia[substring] = 1

    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in frecuencia.items() if count == 1]

    return substrings_unicos


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))

    substrings = obtener_substrings_unicos(string, n)

    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")
