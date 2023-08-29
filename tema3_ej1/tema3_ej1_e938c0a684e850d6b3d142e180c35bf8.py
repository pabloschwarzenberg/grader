# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    
    sumita = 0
    for divisor in divisores:
        sumita = sumita + divisor
    if sumita == 1:
        Primo = True
        return sumita, Primo
    else:
        Primo = False
        return sumita, Primo
           