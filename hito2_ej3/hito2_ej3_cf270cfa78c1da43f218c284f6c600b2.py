def obtener_substrings_unicos(s, n):
    substrings = set()
    count = {}

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    for substring, freq in count.items():
        if freq == 1:
            substrings.add(substring)

    return substrings


if __name__ == "__main__":
    s = input("Ingresa el string: ")
    n = int(input("Ingresa el entero n: "))

    resultados = obtener_substrings_unicos(s, n)

    if len(resultados) > 0:
        for substring in resultados:
            print(substring)
    else:
        print("ninguna")
