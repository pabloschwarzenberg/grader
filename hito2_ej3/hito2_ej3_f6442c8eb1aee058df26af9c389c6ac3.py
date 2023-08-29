def encontrar_subsecuencias_unicas(secuencia, n):
    # Crear un diccionario para contar la frecuencia de las subsecuencias
    frecuencia_subsecuencias = {}

    # Recorrer todas las subsecuencias de longitud n
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in frecuencia_subsecuencias:
            frecuencia_subsecuencias[subsecuencia] += 1
        else:
            frecuencia_subsecuencias[subsecuencia] = 1

    # Encontrar las subsecuencias únicas
    subsecuencias_unicas = [subsecuencia for subsecuencia, frecuencia in frecuencia_subsecuencias.items() if frecuencia == 1]

    return subsecuencias_unicas

# Obtener la secuencia y el valor de n del usuario
secuencia_input = input("Ingresa la secuencia: ")
n_input = int(input("Ingresa el valor de n: "))

# Encontrar las subsecuencias únicas
subsecuencias_unicas = encontrar_subsecuencias_unicas(secuencia_input, n_input)

# Mostrar las subsecuencias únicas encontradas
if len(subsecuencias_unicas) > 0:
    for subsecuencia in subsecuencias_unicas:
        print(subsecuencia)
else:
    print("ninguna")
