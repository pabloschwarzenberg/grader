# completa el código de la función
def suma_divisores(a):
    divisores = [i for i in range(1, a+1) if a % i == 0 ]
    return sum(divisores)
           