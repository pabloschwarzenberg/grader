def encontrar_substrings_unicos(s, n):
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if s.count(sub) == 1:
            substrings.add(sub)
    
    return substrings


def valores():
    s = input("Ingrese el string: ").upper()
    n = int(input("Ingrese el valor de n: "))
    
    listasubstring = encontrar_substrings_unicos(s, n)
    
    if listasubstring:
        for substring in listasubstring:
            print(substring)
    else:
        print("ninguna")

if __name__ == "__main__":
    valores()
