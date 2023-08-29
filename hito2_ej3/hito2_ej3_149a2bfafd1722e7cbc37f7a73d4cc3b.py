def encontrar_substrings_unicos(s, n):
    substrings = []
    counts = {}

    # Generar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in counts:
            counts[substring] += 1
        else:
            counts[substring] = 1

    # Filtrar los substrings únicos
    for substring, count in counts.items():
        if count == 1:
            substrings.append(substring)

    return substrings


if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))

    substrings_unicos = encontrar_substrings_unicos(s, n)

    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
     