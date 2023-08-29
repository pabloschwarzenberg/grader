def obtener_substrings_unicos(secuencia, n):
    substrings = {}
    
    # Obtener todos los substrings de longitud n y contar su frecuencia
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        if substring in substrings:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
    
    # Filtrar los substrings únicos
    substrings_unicos = [substring for substring, count in substrings.items() if count == 1]
    
    return substrings_unicos

# Ejemplo de uso
entrada = input("Ingrese la secuencia de caracteres: ")
n = int(input("Ingrese el tamaño de los substrings: "))

substrings_unicos = obtener_substrings_unicos(entrada, n)

if len(substrings_unicos) > 0:
    for substring in substrings_unicos:
        print(substring)
else:
    print("ninguna")
     