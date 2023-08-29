def encontrar_substrings_unicos(cadena, n):
    substrings = {}
    
    # Generar todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        substring = cadena[i:i+n]
        if substring not in substrings:
            substrings[substring] = 1
        else:
            substrings[substring] += 1
    
    # Filtrar los substrings únicos
    substrings_unicos = [substring for substring in substrings if substrings[substring] == 1]
    
    return substrings_unicos

cadena = input("Ingrese la cadena: ")
n = int(input("Ingrese la longitud de los substrings: "))

substrings_unicos = encontrar_substrings_unicos(cadena, n)

if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
