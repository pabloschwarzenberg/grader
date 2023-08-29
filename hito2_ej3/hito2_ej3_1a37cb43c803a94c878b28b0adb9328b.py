def find_unique_substrings(s, n):
    substrings = set()
    unique_substrings = set()
    
    # Generar todos los substrings de largo n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        substrings.add(substring)
    
    # Verificar si cada substring es único
    for substring in substrings:
        if s.count(substring) == 1:
            unique_substrings.add(substring)
    
    return unique_substrings


if __name__ == "__main__":
    # Obtener el string y el valor de n desde el usuario
    s = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    # Encontrar los substrings únicos de largo n
    unique_substrings = find_unique_substrings(s, n)
    
    # Imprimir los resultados
    if unique_substrings:
        for substring in sorted(unique_substrings):
            print(substring)
    else:
        print("ninguna")
