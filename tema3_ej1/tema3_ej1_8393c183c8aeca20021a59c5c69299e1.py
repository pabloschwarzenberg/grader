def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    
    sumar = 0
    for divisor in divisores:
        sumar += divisor
    if sumar == 1:
        primo = True
        return sumar, primo
    else:
        primo = False
        return sumar, primo