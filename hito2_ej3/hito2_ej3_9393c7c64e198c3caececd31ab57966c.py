def encontrar_substrings_unicos(s, n):
    substrings = set()
    resultados = []

    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring not in substrings:
            substrings.add(substring)
            resultados.append(substring)

    return resultados

if __name__ == "__main__":
    s = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))

    resultados = encontrar_substrings_unicos(s, n)

    if len(resultados) > 0:
        for resultado in resultados:
            print(resultado)
    else:
        print("ninguna")
      