def imprimir_substrings_unicos(s, n):
    substrings = set()
    resultado = []
    
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            resultado.append(substring)
        else:
            substrings.add(substring)
    
    if resultado:
        for substring in set(resultado):
            print(substring)
    else:
        print("ninguna")


if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese la longitud de los substrings: "))
    imprimir_substrings_unicos(s, n)