def imprimir_substrings_unicos(s, n):
    substrings = set()  # Conjunto para almacenar los substrings únicos
    count = {}  # Diccionario para contar la frecuencia de cada substring
    
    # Generar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1
    
    # Filtrar los substrings únicos
    for substring, freq in count.items():
        if freq == 1:
            substrings.add(substring)
    
    # Imprimir los substrings únicos
    if len(substrings) == 0:
        print("ninguna")
    else:
        for substring in substrings:
            print(substring)

# Ejemplos de uso
imprimir_substrings_unicos("ACGACG", 3)  # Imprime "CGA" y "GAC"
imprimir_substrings_unicos("ACGACGAC", 3)  # Imprime "ninguna"
imprimir_substrings_unicos("AAAAA", 3)  # Imprime "ninguna"
