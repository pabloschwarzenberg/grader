# completa el código de la función
def suma_divisores(r):
    divisores = []
    for i in range(1, r):
        if r%i == 0:
            i = divisores.append(i)
    
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        Primo = True
        return suma, Primo
    else:
        Primo = False
        return suma, Primo
           