def validar(ADN, n):
    ADN = ADN.upper()
    secuencia = largo(ADN, n)
    return secuencia
def largo(ADN, n):
    distinto = 0
    linea = []
    largo = len(ADN) - n
    for i in range(largo):
        iguales = distinto
        secuencia = ADN[i:i+n]
        secuencia_leida = ADN.replace(secuencia[0], "-"*n, 1)
        for j in range(len(ADN)):
            secuencia_leida_2 = secuencia_leida[j:j + n]
            if secuencia_leida_2 == secuencia:
                iguales += 1
                break
        if distinto == iguales:
            linea.append(secuencia)
    if not linea:
        linea.append("ninguna")
    return linea
ADN = input()
n = int(input())
print(validar(ADN, n))  