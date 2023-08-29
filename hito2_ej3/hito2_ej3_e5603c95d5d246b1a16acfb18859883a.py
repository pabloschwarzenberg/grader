def obtener_substrings_unicos(s, n):
    substrings = set()
    resultado = []

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if s.count(substring) == 1:
            substrings.add(substring)

    for substring in substrings:
        resultado.append(substring)

    return resultado

if __name__ == "__main__":
    s = input("Ingrese un string: ")
    n = int(input("Ingrese un entero n: "))

    substrings_unicos = obtener_substrings_unicos(s, n)

    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
