      def encontrar_substrings_unicos(s, n):
    substrings = []
    count = {}

    # Recorrer la cadena y contar la frecuencia de cada substring de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        count[substring] = count.get(substring, 0) + 1

    # Filtrar los substrings que aparecen solo una vez
    for substring, freq in count.items():
        if freq == 1:
            substrings.append(substring)

    return substrings


if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese la longitud de los substrings: "))

    unique_substrings = encontrar_substrings_unicos(s, n)

    if len(unique_substrings) > 0:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")
