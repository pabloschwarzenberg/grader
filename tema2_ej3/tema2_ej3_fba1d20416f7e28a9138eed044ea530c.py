def numero_perfecto(a):
    sumdiv = 0
    estado = False
    divisores = [i for i in range(1, a) if a % i == 0]
    for i in range(len(divisores)):
        sumdiv += divisores[i]
    if a == sumdiv:
        estado = True

    return estado          