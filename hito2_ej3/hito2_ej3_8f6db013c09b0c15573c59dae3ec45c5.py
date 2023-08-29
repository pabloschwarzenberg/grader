
def obtener_substrings_unicos(string, n):
    substrings = []
    unique_substrings = []
    
    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substrings.append(string[i:i+n])
    
    # Encontrar los substrings que aparecen una única vez
    for substring in substrings:
        if substrings.count(substring) == 1:
            unique_substrings.append(substring)
    
    return unique_substrings

# Solicitar entrada al usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos
substrings_unicos = obtener_substrings_unicos(string, n)

# Imprimir los substrings únicos encontrados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")