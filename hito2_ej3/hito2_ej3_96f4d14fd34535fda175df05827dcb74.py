def find_unique_substrings(s, n):
    substr_count = {}
    unique_substrings = []
    
    # Iterar sobre los substrings de largo n en la cadena s
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        
        # Contar la aparición de cada substring
        if substring in substr_count:
            substr_count[substring] += 1
        else:
            substr_count[substring] = 1
    
    # Obtener los substrings únicos de largo n
    for substring, count in substr_count.items():
        if count == 1:
            unique_substrings.append(substring)
    
    return unique_substrings

# Obtener la entrada del usuario
s = input("Ingresa una cadena: ")
n = int(input("Ingresa un número entero: "))

# Encontrar los substrings únicos
unique_substrings = find_unique_substrings(s, n)

# Imprimir los resultados
if len(unique_substrings) > 0:
    for substring in unique_substrings:
        print(substring)
else:
    print("ninguna")
