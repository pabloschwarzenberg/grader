def encontrar_subcadenas_unicas(cadena, n):
    subcadenas = set()
    subcadenas_unicas = []

    for i in range(len(cadena) - n + 1):
        subcadena = cadena[i:i+n]
        if subcadena in subcadenas:
            if subcadena in subcadenas_unicas:
                subcadenas_unicas.remove(subcadena)
        else:
            subcadenas.add(subcadena)
            subcadenas_unicas.append(subcadena)

    return subcadenas_unicas

# Obtener la cadena y el valor de n del usuario
cadena_input = input("Ingrese una cadena de texto: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subcadenas únicas de longitud n
subcadenas_unicas = encontrar_subcadenas_unicas(cadena_input, n)

# Imprimir las subcadenas únicas encontradas
if subcadenas_unicas:
    for subcadena in subcadenas_unicas:
        print(subcadena)
else:
    print("ninguna")
