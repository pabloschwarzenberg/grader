def numero_perfecto(a):
    sumaDivisores = 0
    for i in range(1,a):
        if a % i == 0:
            sumaDivisores = sumaDivisores + i
    if sumaDivisores == a:
        numeroPerfecto = True
    else:
        numeroPerfecto = False
    return numeroPerfecto