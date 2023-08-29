def encontrar_substrings_unicos(secuencia, n):
    substrings = set()
    substring_unicos = set()

    # Obtener todos los substrings de longitud n
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        substrings.add(substring)

    # Verificar si cada substring aparece una única vez
    for substring in substrings:
        if secuencia.count(substring) == 1:
            substring_unicos.add(substring)

    return substring_unicos


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el valor de n: "))

    substrings_unicos = encontrar_substrings_unicos(secuencia, n)

    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
    