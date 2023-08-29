def obtener_substrings_unicos(string, n):
    substrings = []
    contador = {}


    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        substrings.append(substring)
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1


    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]

    return substrings_unicos


cadena = input("Ingrese una cadena: ")
n = int(input("Ingrese el valor de n: "))


substrings_unicos = obtener_substrings_unicos(cadena, n)


if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")      