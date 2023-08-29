def encontrar_subsecuencias_unicas(secuencia, n):
    subsecuencias = []
    contador = {}

    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        subsecuencias.append(subsecuencia)
        if subsecuencia in contador:
            contador[subsecuencia] += 1
        else:
            contador[subsecuencia] = 1
    
    subsecuencias_unicas = [subsecuencia for subsecuencia in subsecuencias if contador[subsecuencia] == 1]
    
    return subsecuencias_unicas

secuencia = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

subsecuencias = encontrar_subsecuencias_unicas(secuencia, n)

if len(subsecuencias) == 0:
    print("ninguna")
else:
    for subsecuencia in subsecuencias:
        print(subsecuencia)    