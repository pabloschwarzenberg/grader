def encontrar_subsecuencias_unicas(secuencia, n):

    subsecuencias = {}


    for i in range(len(secuencia) - n + 1):
        subsecuencia = secuencia[i:i+n]
        if subsecuencia in subsecuencias:
            subsecuencias[subsecuencia] += 1
        else:
            subsecuencias[subsecuencia] = 1


    return [subsecuencia for subsecuencia, count in subsecuencias.items() if count == 1]


secuencia = input('Ingresa la secuencia de ADN: ')
n = int(input('Ingresa el valor de n: '))


subsecuencias_unicas = encontrar_subsecuencias_unicas(secuencia, n)


if len(subsecuencias_unicas) == 0:
    print('ninguna')
else:
    for subsecuencia in subsecuencias_unicas:
        print(subsecuencia)