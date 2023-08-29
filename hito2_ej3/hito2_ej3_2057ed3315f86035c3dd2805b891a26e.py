def encontrar_substrings_unicos(secuencia, n):
    substrings = set()
    ocurrencias = {}

    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in ocurrencias:
            ocurrencias[substring] += 1
            substrings.discard(substring)
        else:
            ocurrencias[substring] = 1
            substrings.add(substring)

    return substrings


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el valor de n: "))

    resultados = encontrar_substrings_unicos(secuencia, n)

    if resultados:
        for substring in resultados:
            print(substring)
    else:
        print("ninguna")
