def encontrar_substrings(string, n):
    substrings = []
    count = {}
    
    # Construir un diccionario con la frecuencia de cada substring de longitud n
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        count[substring] = count.get(substring, 0) + 1
    
    # Obtener los substrings únicos
    for substring, frequency in count.items():
        if frequency == 1:
            substrings.append(substring)
    
    return substrings


if __name__ == "__main__":
    entrada = input("Ingrese un string y un entero n separados por espacio: ")
    partes = entrada.split()
    
    string = partes[0]
    n = int(partes[1])
    
    substrings = encontrar_substrings(string, n)
    
    if substrings:
        for substring in substrings:
            print(substring)
    else:
        print("ninguna")
