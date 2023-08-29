def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    
   
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        esPrimo = True
        return suma, esPrimo
    else:
        esPrimo = False
        return suma, esPrimo
         
    
           