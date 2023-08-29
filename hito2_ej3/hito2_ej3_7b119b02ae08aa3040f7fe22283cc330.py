def encontrar_substrings_unicos(string, n):
    substrings = set()
    contador = {}
    
    # Obtener todos los substrings de largo n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        substrings.add(substring)
        contador[substring] = contador.get(substring, 0) + 1
    
    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]
    
    return substrings_unicos


if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings_unicos = encontrar_substrings_unicos(string, n)
    
    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
      