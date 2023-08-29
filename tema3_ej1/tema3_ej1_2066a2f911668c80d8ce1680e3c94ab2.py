# completa el código de la función
def sumaDivisores(a):
    divisores = []
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
            
    suma = 0
    for divisor in divisores:
        suma += divisor
    
    if suma == 1:
        primo = True
        return suma, primo
    else:
        primo = False
        return suma, primo  