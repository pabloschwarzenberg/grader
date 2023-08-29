def encontrar_substrings_unicos(cadena, n):
    substrings = set()  # Conjunto para almacenar los substrings únicos
    duplicados = set()  # Conjunto para almacenar los substrings duplicados

    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]  # Obtener el substring de longitud n

        if substring in substrings:
            duplicados.add(substring)  # Agregar el substring a los duplicados
        else:
            substrings.add(substring)  # Agregar el substring a los únicos

    substrings_unicos = substrings - duplicados  # Obtener los substrings únicos

    return substrings_unicos

if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    n = int(input("Ingrese el tamaño de los substrings: "))

    substrings = encontrar_substrings_unicos(cadena, n)

    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")
      