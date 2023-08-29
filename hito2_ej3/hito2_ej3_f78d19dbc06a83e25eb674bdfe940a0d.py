def obtener_substrings_unicos(s, n):
    substrings = {}
    
    # Obtener todos los substrings de largo n
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if substring not in substrings:
            substrings[substring] = 1
        else:
            substrings[substring] += 1
    
    # Filtrar los substrings únicos
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    return substrings_unicos

# Obtener el string y el entero n desde el usuario
s = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Obtener los substrings únicos de largo n
substrings_unicos = obtener_substrings_unicos(s, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
