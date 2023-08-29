def obtener_substrings_unicos(s, n):
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if s.count(substring) == 1:
            substrings.add(substring)
    return substrings

if __name__ == "__main__":
    s = input("Ingrese la cadena: ")
    n = int(input("Ingrese el valor de n: "))
    
    unique_substrings = obtener_substrings_unicos(s, n)
    
    if len(unique_substrings) > 0:
        for substring in unique_substrings:
            print(substring)
    else:
        print("ninguna")