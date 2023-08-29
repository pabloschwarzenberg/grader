def obtener_substrings_unicos(string, n):
    substrings = {}
    
    # Obtener todos los substrings de largo n y contar su frecuencia
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr in substrings:
            substrings[substr] += 1
        else:
            substrings[substr] = 1
    
    # Filtrar los substrings únicos
    substrings_unicos = [substr for substr, count in substrings.items() if count == 1]
    
    return substrings_unicos


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings_unicos = obtener_substrings_unicos(string, n)
    
    if len(substrings_unicos) > 0:
        for substr in substrings_unicos:
            print(substr)
    else:
        print("ninguna")