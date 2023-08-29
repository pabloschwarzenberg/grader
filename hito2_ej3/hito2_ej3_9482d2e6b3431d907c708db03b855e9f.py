def encontrar_substrings_unicos(secuencia, n):
    substrings = {}
    
    # Recorrer la secuencia y encontrar todos los substrings de longitud n
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    
    return substrings_unicos

if __name__ == "__main__":
    # Leer la secuencia y la longitud n desde la entrada estándar
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese la longitud de los substrings: "))
    
    # Encontrar los substrings únicos
    substrings_unicos = encontrar_substrings_unicos(secuencia, n)
    
    # Imprimir los resultados
    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
