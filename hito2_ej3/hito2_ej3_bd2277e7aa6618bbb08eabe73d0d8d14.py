def encontrar_substrings_unicos(secuencia, n):
    substrings = {}
    
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    
    return substrings_unicos

entrada = input("Introduce la secuencia: ")
n = int(input("Introduce el valor de n: "))

substrings_unicos = encontrar_substrings_unicos(entrada, n)

if substrings_unicos:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
