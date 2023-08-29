def unico_substrings(s, n):
    substrings = {}
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    unico_substrings = [substring for substring, count in substrings.items() if count == 1]
    return unico_substrings

s = input("Ingrese el string: ")
n = int(input("Ingrese el numero entero: "))

resultados = unico_substrings(s, n)
if resultados:
    for substring in resultados:
        print(substring)
else:
    print("ninguna")
