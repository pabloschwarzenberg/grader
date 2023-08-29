def numero_perfecto(a):
    divisores = 1
    divisor = 2
    while divisor <= a:
        if a % divisor == 0:
            divisores += divisor
        divisor += 1
    divisores -= a
    if divisores == a:
        return True
    elif divisores != a:
        return False