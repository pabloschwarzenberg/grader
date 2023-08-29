# completa el código de la función
def suma_divisores(a):
    aux = a
    factores = []
    i = 2
    while (aux > 1):
        if aux % i == 0:
            factor = i
            aux /= factor
            if factor not in factores:
                factores.append(factor)
        else:
            i += 1

    aux = a
    potencias = []
    potencia = 0
    j = 0
    while (j < len(factores)):
        if (aux % factores[j] == 0):
            potencia += 1
            aux /= factores[j]
        else:
            potencias.append(potencia)
            potencia = 0
            j += 1

    resultado = 1
    for i in range(len(factores)):
        resultado *= (factores[i] ** (potencias[i] + 1) - 1) / (factores[i] - 1)

    resultado = resultado - a
    if resultado == 1:
        respuesta = True
    else:
        if resultado % 2 == 0:
            respuesta = False
        else:
            respuesta = True
    if a == 1:
        respuesta = False

    return resultado