def encontrar_subsecuencias_unicas(secuencia, n):
    subsecuencias = {}
    
    # Iterar sobre todas las subsecuencias de longitud n en la secuencia
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        
        # Verificar si la subsecuencia ya existe en el diccionario
        if subsecuencia in subsecuencias:
            subsecuencias[subsecuencia] += 1
        else:
            subsecuencias[subsecuencia] = 1
    
    # Filtrar las subsecuencias únicas
    subsecuencias_unicas = [subsecuencia for subsecuencia, count in subsecuencias.items() if count == 1]
    
    return subsecuencias_unicas

# Solicitar la secuencia y el valor de n al usuario
secuencia = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subsecuencias únicas de longitud n
subsecuencias = encontrar_subsecuencias_unicas(secuencia, n)

# Imprimir el resultado
if len(subsecuencias) > 0:
    for subsecuencia in subsecuencias:
        print(subsecuencia)
else:
    print("ninguna")
      