def encontrar_substrings_unicos(cadena, n):
    subcadenas = set()
    subcadenas_unicas = []

    for i in range(len(cadena) - n + 1):
        subcadena = cadena[i:i+n]
        subcadenas.add(subcadena)

    for subcadena in subcadenas:
        if cadena.count(subcadena) == 1:
            subcadenas_unicas.append(subcadena)

    return subcadenas_unicas

cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

subcadenas_unicas = encontrar_substrings_unicos(cadena, n)

if cadena.count(cadena[0]) == len(cadena):
    print("ninguna")
elif len(subcadenas_unicas) > 0:
    for subcadena in subcadenas_unicas:
        print(subcadena)
else:
    print("ninguna")