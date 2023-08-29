def obtener_substrings_unicos(s, n):
    substrings = set()
    contador = {}
    
    # Recorrer el string y contar la frecuencia de cada substring de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1
    
    # Obtener los substrings únicos que aparecen una sola vez
    for substring, count in contador.items():
        if count == 1:
            substrings.add(substring)
    
    # Imprimir los substrings únicos encontrados
    if len(substrings) > 0:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")

# Ejemplos de uso
obtener_substrings_unicos("ACGACG", 3)  # Salida: CGA, GAC
obtener_substrings_unicos("ACGACGAC", 3)  # Salida: ninguna
obtener_substrings_unicos("AAAAA", 3)  # Salida: ninguna
      