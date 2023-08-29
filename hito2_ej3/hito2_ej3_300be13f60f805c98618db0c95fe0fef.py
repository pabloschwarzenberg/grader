def obtener_substrings_unicos(s, n):
    substrings = set()
    contador = {}
    
    # Recorre todos los substrings de longitud n en la cadena s
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1

    # Filtra los substrings que aparecen una única vez
    for substring, count in contador.items():
        if count == 1:
            substrings.add(substring)
    
    return substrings

# Obtener la entrada del usuario
s = input("Ingrese una cadena: ")
n = int(input("Ingrese un entero: "))

# Obtener los substrings únicos de longitud n
substrings_unicos = obtener_substrings_unicos(s, n)

# Imprimir los substrings únicos encontrados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      