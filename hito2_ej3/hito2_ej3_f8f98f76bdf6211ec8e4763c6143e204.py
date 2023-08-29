def obtener_substrings_unicos(string, n):
    substrings = {}
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    
    return substrings_unicos


string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

substrings_unicos = obtener_substrings_unicos(string, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")      