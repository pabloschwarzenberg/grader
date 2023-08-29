def encontrar_substrings_unicos(secuencia, n):
    substrings = set()
    resultado = []
    
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            substrings.remove(substring)
        else:
            substrings.add(substring)
    
    for substring in substrings:
        resultado.append(substring)
    
    return resultado

# Obtener la secuencia y el valor de n del usuario
secuencia_ingresada = input("Ingrese la secuencia: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos
substrings_unicos = encontrar_substrings_unicos(secuencia_ingresada, n)

# Imprimir los resultados
if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
