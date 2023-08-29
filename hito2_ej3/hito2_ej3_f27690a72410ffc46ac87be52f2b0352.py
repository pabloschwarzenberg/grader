def encontrar_subsecuencias_unicas(secuencia, n):
    subsecuencias = set()
    subsecuencias_repetidas = set()

    # Recorrer la secuencia y encontrar las subsecuencias de longitud n
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i + n]
        if subsecuencia in subsecuencias:
            subsecuencias_repetidas.add(subsecuencia)
        else:
            subsecuencias.add(subsecuencia)

    # Filtrar las subsecuencias únicas
    subsecuencias_unicas = subsecuencias - subsecuencias_repetidas

    return subsecuencias_unicas

# Obtener la secuencia de ADN y el valor de n desde el usuario
secuencia_adn = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subsecuencias únicas de longitud n
subsecuencias = encontrar_subsecuencias_unicas(secuencia_adn, n)

# Imprimir las subsecuencias únicas encontradas
if len(subsecuencias) == 0:
    print("ninguna")
else:
    for subsecuencia in subsecuencias:
        print(subsecuencia)
