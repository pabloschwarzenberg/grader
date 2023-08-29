def obtener_substrings_unicos(cadena, n):
    substrings = set()
    repetidos = set()
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring in substrings:
            repetidos.add(substring)
        else:
            substrings.add(substring)

    unicos = substrings - repetidos
    return unicos

cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = obtener_substrings_unicos(cadena, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      