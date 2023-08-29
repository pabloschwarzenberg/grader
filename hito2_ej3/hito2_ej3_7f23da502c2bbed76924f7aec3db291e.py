def encontrar_subsecuencias_unicas(string, n):
    subsecuencias = []
    contador = {}

    for i in range(len(string) - n + 1):
        subsecuencia = string[i:i+n]
        if subsecuencia not in contador:
            contador[subsecuencia] = 1
        else:
            contador[subsecuencia] += 1

    for subsecuencia, count in contador.items():
        if count == 1:
            subsecuencias.append(subsecuencia)

    return subsecuencias

# Obtener el string y el valor de n como entrada del usuario
string = input("Ingrese el string: ")
n = int(input("Ingrese el valor de n: "))

# Encontrar las subsecuencias únicas de largo n
subsecuencias_unicas = encontrar_subsecuencias_unicas(string, n)

# Imprimir el resultado
if len(subsecuencias_unicas) > 0:
    print("Subsecuencias únicas de largo", n, ":")
    for subsecuencia in subsecuencias_unicas:
        print(subsecuencia)
else:
    print("ninguna")

   