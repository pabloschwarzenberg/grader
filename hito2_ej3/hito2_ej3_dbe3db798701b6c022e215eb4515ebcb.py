def encontrar_substrings_unicos(s, n):
    substrings = {}
    
    # Recorrer la cadena y encontrar todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    
    return substrings_unicos


if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))
    
    unique_substrings = encontrar_substrings_unicos(s, n)
    
    if len(unique_substrings) == 0:
        print("ninguna")
    else:
        for substring in unique_substrings:
            print(substring)