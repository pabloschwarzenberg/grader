def numero_perfecto(n):
    divisores = []
    for x in range(1, n):
        if n%x == 0:
            x = divisores.append(x)
    
   
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == n:
        NumeroPerfecto = True
    else:
        NumeroPerfecto = False
    return NumeroPerfecto           