def obtener_substrings_unicos(secuencia, n):
    substrings = []
    contador = {}
    
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1
    
    for substring, count in contador.items():
        if count == 1:
            substrings.append(substring)
    
    return substrings


if __name__ == "__main__":
    secuencia = input("Ingrese la secuencia: ")
    n = int(input("Ingrese el tamaño de los substrings: "))
    
    substrings_unicos = obtener_substrings_unicos(secuencia, n)
    
    if len(substrings_unicos) > 0:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")