def imprimir_substrings_unicos(s, n):
    substrings = {}

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1

    encontrados = False

    for substring, count in substrings.items():
        if count == 1:
            print(substring)
            encontrados = True

    if not encontrados:
        print("ninguna")

if __name__ == "__main__":
    s = input("Ingrese la secuencia: ")
    n = int(input("Ingrese la longitud de los substrings: "))

    imprimir_substrings_unicos(s, n)
      