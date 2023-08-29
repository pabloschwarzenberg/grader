def numero_perfecto(a):
    divisores = []
    indice = 0
    resultado = 0
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
        while indice < len(divisores):
            resultado = resultado + divisores[indice]
            indice = indice + 1
    if resultado == a:
        return True
    else:
        return False

           