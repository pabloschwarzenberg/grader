def numero_perfecto(a):
    resultado = 0
    for divisores in range(1, a):
        if a % divisores == 0:
            resultado += divisores
    if resultado == a:
        return True
    else:
        return False
