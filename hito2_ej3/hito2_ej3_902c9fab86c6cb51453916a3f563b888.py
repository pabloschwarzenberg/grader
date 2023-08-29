def obtener_subsecuencias_unicas(secuencia, n):
    subsecuencias = set()
    subsecuencias_unicas = set()

    # Obtener todas las subsecuencias de longitud n
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in subsecuencias:
            subsecuencias_unicas.discard(subsecuencia)
        else:
            subsecuencias.add(subsecuencia)
            subsecuencias_unicas.add(subsecuencia)

    return subsecuencias_unicas

# Obtener la secuencia y el valor de n desde el usuario
secuencia = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Obtener las subsecuencias únicas de longitud n
subsecuencias_unicas = obtener_subsecuencias_unicas(secuencia, n)

# Imprimir las subsecuencias únicas
if len(subsecuencias_unicas) == 0:
    print("ninguna")
else:
    for subsecuencia in subsecuencias_unicas:
        print(subsecuencia)     