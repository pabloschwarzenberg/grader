def obtener_substrings_unicos(string, n):
    substrings = set()
    unique_substrings = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            unique_substrings.discard(substring)
        else:
            substrings.add(substring)
            unique_substrings.add(substring)
    
    return unique_substrings

if __name__ == "__main__":
    string = input("Ingrese el string: ")
    n = int(input("Ingrese el valor de n: "))
    
    substrings_unicos = obtener_substrings_unicos(string, n)
    
    if substrings_unicos:
        for substring in substrings_unicos:
            print(substring)
    else:
        print("ninguna")
