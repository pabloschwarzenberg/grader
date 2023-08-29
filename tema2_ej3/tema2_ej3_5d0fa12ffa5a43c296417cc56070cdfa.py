def numero_perfecto(a):
    sumador = 0
    for num in range(1,a-1):
        restodiv = a%num
        if restodiv == 0:
            sumador = sumador+num
    if sumador == a:
        Num_perfecto = True
    else:
        Num_perfecto = False

    return Num_perfecto
