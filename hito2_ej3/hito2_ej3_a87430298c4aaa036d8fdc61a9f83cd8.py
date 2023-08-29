def obtener_subsecuencias(cadena, n):
    subsecuencias = []
    contador = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(cadena) - n + 1):
        subsecuencia = cadena[i:i+n]
        subsecuencias.append(subsecuencia)

        # Contar la aparición de cada subsecuencia
        if subsecuencia in contador:
            contador[subsecuencia] += 1
        else:
            contador[subsecuencia] = 1

    # Filtrar las subsecuencias que aparecen solo una vez
    subsecuencias_unicas = [subsecuencia for subsecuencia in subsecuencias if contador[subsecuencia] == 1]

    return subsecuencias_unicas

# Obtener la cadena de ADN y el número n del usuario
cadena_adn = input("Ingrese la cadena de ADN: ")
n = int(input("Ingrese la longitud de los substrings: "))

# Obtener y mostrar las subsecuencias únicas de longitud n
subsecuencias = obtener_subsecuencias(cadena_adn, n)

if len(subsecuencias) > 0:
    for subsecuencia in subsecuencias:
        print(subsecuencia)
else:
    print("ninguna")
