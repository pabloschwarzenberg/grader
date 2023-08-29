# completa el código de la función
def suma_divisores(n):
    divisoresN = []
    for x in range(1, n):
        if n%x == 0:
            x = divisoresN.append(x)
    
   
    suma = 0
    for divisor in divisoresN:
        suma = suma + divisor
    if suma == 1:
        Nprimo = True
        return suma, Nprimo
    else:
        Nprimo = False
        return suma, Nprimo