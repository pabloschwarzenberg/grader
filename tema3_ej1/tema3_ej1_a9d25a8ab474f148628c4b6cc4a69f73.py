# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    
    ##sumar divisores
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        es_Primo = True
        return suma, es_Primo
    else:
        es_Primo = False
        return suma, es_Primo