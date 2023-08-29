def numero_perfecto(n):
    i = 1
    acumulador = 0
    while i < n:
        if n % i == 0:
            acumulador = acumulador+i
        i = i+1
    if acumulador == n:
        return True
    else:
        return False

           