def obtener_substrings_unicos(s, n):
    substrings = []
    contador = {}
    
    # Recorrer todos los substrings de largo n en la cadena s
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        
        # Incrementar el contador para el substring actual
        contador[substring] = contador.get(substring, 0) + 1
    
    # Filtrar los substrings que aparecen una única vez
    for substring, count in contador.items():
        if count == 1:
            substrings.append(substring)
    
    return substrings


if __name__ == "__main__":
    s = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings_unicos = obtener_substrings_unicos(s, n)
    
    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")


