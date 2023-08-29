def encontrar_substrings_unicos(secuencia, n):
    # Crear un diccionario para almacenar la frecuencia de los substrings
    frecuencia = {}
    
    # Obtener todos los substrings de longitud n
    for i in range(len(secuencia) - n + 1):
        substring = secuencia[i:i+n]
        
        # Incrementar la frecuencia del substring en el diccionario
        frecuencia[substring] = frecuencia.get(substring, 0) + 1
    
    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substring for substring, count in frecuencia.items() if count == 1]
    
    return substrings_unicos

# Obtener la secuencia del usuario
secuencia = input("Ingrese una secuencia de ADN: ")
# Obtener el valor de n del usuario
n = int(input("Ingrese el valor de n: "))

# Encontrar los substrings únicos de longitud n en la secuencia
substrings = encontrar_substrings_unicos(secuencia, n)

# Imprimir los substrings únicos encontrados
if len(substrings) == 0:
    print("ninguna")
else:
    for substring in substrings:
        print(substring)
