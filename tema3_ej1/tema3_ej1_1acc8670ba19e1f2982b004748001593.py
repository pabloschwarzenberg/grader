def suma_divisores(a):
    suma = 0
    divisor = a
    while divisor > 1:
        divisor = divisor - 1
        if (a % divisor) == 0:
            suma += divisor
    else:
        for n in range(2, a):
            if a % n == 0:   #if n >= a:
                return False
            else:
                return True
        return suma