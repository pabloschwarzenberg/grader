def encontrar_substrings_unicos(secuencia, n):
    substrings = {}
    for i in range(len(secuencia) - n + 1):
        substr = secuencia[i:i+n]
        if substr in substrings:
            substrings[substr] += 1
        else:
            substrings[substr] = 1

    unique_substrings = [substr for substr, count in substrings.items() if count == 1]
    return unique_substrings


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese la longitud del substring (n): "))

    unique_substrings = encontrar_substrings_unicos(secuencia, n)
    if unique_substrings:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")
