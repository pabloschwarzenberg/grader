def numero_perfecto(a):
    sum = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            sum += divisor
    if sum==a:
        return True
    if sum !=a:
        return False

