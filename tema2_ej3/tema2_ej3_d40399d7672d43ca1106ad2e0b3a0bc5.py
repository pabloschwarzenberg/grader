def numero_perfecto(a,n_p = False):
    suma = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            suma += divisor
    if suma == a:
        n_p = True
    return n_p
           