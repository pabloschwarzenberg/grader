def encontrar_substrings_unicos(cadena, n):
    sub_cadenas = []
    count = {}
    for i in range(len(cadena) - n + 1):
        subcadena = cadena[i:i+n]
        if subcadena in count:
            count[subcadena] += 1
        else:
            count[subcadena] = 1

    for subcadena, ocurrencias in count.items():
        if ocurrencias == 1:
            sub_cadenas.append(subcadena)

    return sub_cadenas


entrada_cadena = input("Ingrese una cadena de texto: ")
entrada_n = int(input("Ingrese el valor de n: "))

substrings_unicos = encontrar_substrings_unicos(entrada_cadena, entrada_n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
