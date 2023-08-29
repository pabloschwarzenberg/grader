def encontrar_subsecuencias(secuencia, n):
    subsecuencias = []
    frecuencias = {}
    
    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in frecuencias:
            frecuencias[subsecuencia] += 1
        else:
            frecuencias[subsecuencia] = 1
    
    for subsecuencia, frecuencia in frecuencias.items():
        if frecuencia == 1:
            subsecuencias.append(subsecuencia)
    
    return subsecuencias


if __name__ == "__main__":
    secuencia = input("Ingresa la secuencia de ADN: ")
    n = int(input("Ingresa el tamaño de las subsecuencias: "))
    
    subsecuencias = encontrar_subsecuencias(secuencia, n)
    
    if len(subsecuencias) > 0:
        for subsecuencia in subsecuencias:
            print(subsecuencia)
    else:
        print("ninguna")
