def obtener_substrings_unicos(s, n):
    substrings = []
    contador = {}

    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    for substring, count in contador.items():
        if count == 1:
            substrings.append(substring)

    return substrings


if __name__ == "__main__":
    s = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))

    substrings_unicos = obtener_substrings_unicos(s, n)

    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")