def obtener_substrings_unicos(s, n):
    substrings = set()
    unicos = set()
    
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            unicos.discard(substring)
        else:
            substrings.add(substring)
            unicos.add(substring)
    
    return unicos

s = input("Ingrese un string: ")
n = int(input("Ingrese un entero: "))

resultado = obtener_substrings_unicos(s, n)

if resultado:
    for substring in resultado:
        print(substring)
else:
    print("ninguna")
