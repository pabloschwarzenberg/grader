def find_unique_substrings(s, n):
    substrings = set()  # Conjunto para almacenar los substrings únicos
    count_map = {}  # Diccionario para contar las ocurrencias de los substrings
    
    # Generar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in count_map:
            count_map[substring] += 1
        else:
            count_map[substring] = 1
    
    # Filtrar los substrings únicos
    for substring, count in count_map.items():
        if count == 1:
            substrings.add(substring)
    
    return substrings

# Solicitar la cadena y el valor de n al usuario
s = input("Ingrese la cadena: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n
substrings = find_unique_substrings(s, n)

# Imprimir los resultados
if substrings:
    for substring in substrings:
        print(substring)
else:
    print("ninguna")     