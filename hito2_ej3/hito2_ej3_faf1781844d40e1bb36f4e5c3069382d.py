def encontrar_substr_unicos(cadena, n):
    substr_count = {}
    resultado = []

    for i in range(len(cadena) - n + 1):
        substr = cadena[i:i+n]

        if substr in substr_count:
            substr_count[substr] += 1
        else:
            substr_count[substr] = 1

    for substr, count in substr_count.items():
        if count == 1:
            resultado.append(substr)

    return resultado

cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = encontrar_substr_unicos(cadena, n)

if len(substrings_unicos) == 0:
    print("ninguna")
else:
    for substr in substrings_unicos:
        print(substr)
      