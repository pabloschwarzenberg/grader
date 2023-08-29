def encontrar_substrings_unicos(secuencia, n):
    substrings = {}
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i + n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    resultados = [substring for substring, count in substrings.items() if count == 1]
    return resultados

if __name__ == "__main__":
    secuencia = input("Ingresa la secuencia: ")
    n = int(input("Ingresa el valor de n: "))

    substrings_unicos = encontrar_substrings_unicos(secuencia, n)

    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
