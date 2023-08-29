def obtener_subsecuencias(s, n):
    subsecuencias = []
    contador = {}
    
    # Obtener todas las subsecuencias de longitud n
    for i in range(len(s) - n + 1):
        subsecuencia = s[i:i+n]
        subsecuencias.append(subsecuencia)
        if subsecuencia in contador:
            contador[subsecuencia] += 1
        else:
            contador[subsecuencia] = 1
    
    # Filtrar las subsecuencias que aparecen una única vez
    subsecuencias_unicas = [subsecuencia for subsecuencia in subsecuencias if contador[subsecuencia] == 1]
    
    return subsecuencias_unicas


# Obtener la secuencia y el valor de n del usuario
secuencia = input("Ingrese la secuencia de ADN: ")
n = int(input("Ingrese el valor de n: "))

# Obtener las subsecuencias únicas de longitud n
subsecuencias = obtener_subsecuencias(secuencia, n)

# Imprimir el resultado
if len(subsecuencias) > 0:
    for subsecuencia in subsecuencias:
        print(subsecuencia)
else:
    print("ninguna")
      