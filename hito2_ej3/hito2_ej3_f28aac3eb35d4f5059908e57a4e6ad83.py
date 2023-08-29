def obtener_substrings_unicos(s, n):
    substrings = set()
    repetidos = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            repetidos.add(substring)
        else:
            substrings.add(substring)
    return substrings - repetidos

if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el tamaño de los substrings: "))

    resultados = obtener_substrings_unicos(s, n)

    if resultados:
        for substring in resultados:
            print(substring)
    else:
        print("ninguna")      