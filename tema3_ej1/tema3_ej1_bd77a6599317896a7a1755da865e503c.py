# completa el código de la función
           
def suma_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    
    return suma(divisores)