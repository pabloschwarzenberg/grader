def obtener_substrings_unicos(secuencia, n):
    substrings = []
    contador = {}
   
    for i in range(len(secuencia)-n+1):
        substring = secuencia[i:i+n]
        substrings.append(substring)
        
        if substring in contador:
            contador[substring] += 1
        else:
            contador[substring] = 1
    
    substrings_unicos = [substring for substring in substrings if contador[substring] == 1]
    return substrings_unicos

entrada = input("Ingrese la secuencia: ")
n = int(input("Ingrese el tamaño de los substrings: "))

substrings_unicos = obtener_substrings_unicos(entrada, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
      