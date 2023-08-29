def obtener_subsecuencias_unicas(secuencia, n):
    subsecuencias = set()
    subsecuencias_repetidas = set()

    # Obtener todas las subsecuencias de largo n
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in subsecuencias:
            subsecuencias_repetidas.add(subsecuencia)
        else:
            subsecuencias.add(subsecuencia)

    # Filtrar las subsecuencias que aparecen una única vez
    subsecuencias_unicas = subsecuencias - subsecuencias_repetidas

    return subsecuencias_unicas

# Obtener la secuencia y el valor de n desde el usuario
secuencia = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Obtener las subsecuencias únicas de largo n
subsecuencias = obtener_subsecuencias_unicas(secuencia, n)

# Imprimir las subsecuencias únicas
if len(subsecuencias) > 0:
    for subsecuencia in subsecuencias:
        print(subsecuencia)
else:
    print("ninguna")
