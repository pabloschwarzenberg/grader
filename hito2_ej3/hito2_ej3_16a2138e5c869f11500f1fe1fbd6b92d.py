def encontrar_substrings_unicos(secuencia, n):
    substrings = set()
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if secuencia.count(substring) == 1:
            substrings.add(substring)
    return substrings

if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el largo de los substrings: "))

    substrings_unicos = encontrar_substrings_unicos(secuencia, n)

    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
      