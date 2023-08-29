def encontrar_subsecuencias_unicas(secuencia, n):
    subsecuencias = set()
    subsecuencias_unicas = set()

    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in subsecuencias:
            subsecuencias_unicas.discard(subsecuencia)
        else:
            subsecuencias.add(subsecuencia)
            subsecuencias_unicas.add(subsecuencia)

    return subsecuencias_unicas

# Solicitar al usuario la secuencia de ADN y el valor de n
secuencia_adn = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subsecuencias únicas de longitud n
subsecuencias_unicas = encontrar_subsecuencias_unicas(secuencia_adn, n)

# Imprimir el resultado
if len(subsecuencias_unicas) > 0:
    for subsecuencia in subsecuencias_unicas:
        print(subsecuencia)
else:
    print("ninguna")
