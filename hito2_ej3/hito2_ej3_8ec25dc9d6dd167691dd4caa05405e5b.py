def obtener_substrings_unicos(cadena, n):
    substrings = {}
    for i in range(len(cadena)-n+1):
        substring = cadena[i:i+n]
        if substring not in substrings:
            substrings[substring] = 1
        else:
            substrings[substring] += 1

    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    return substrings_unicos

cadena = input("Ingrese una cadena: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = obtener_substrings_unicos(cadena, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")