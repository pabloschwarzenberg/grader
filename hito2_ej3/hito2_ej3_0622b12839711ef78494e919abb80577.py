def obtener_substrings(string, n):
    # Crear un diccionario para contar la frecuencia de los substrings de tamaño n
    substrings_frecuencia = {}
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr in substrings_frecuencia:
            substrings_frecuencia[substr] += 1
        else:
            substrings_frecuencia[substr] = 1
    
    # Filtrar los substrings que aparecen una única vez
    substrings_unicos = [substr for substr, frecuencia in substrings_frecuencia.items() if frecuencia == 1]
    
    return substrings_unicos


# Obtener el string y el entero n como entrada del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el entero n: "))

# Obtener los substrings únicos de tamaño n
substrings = obtener_substrings(string, n)

# Imprimir los resultados
if len(substrings) > 0:
    for substr in substrings:
        print(substr)
else:
    print("ninguna")