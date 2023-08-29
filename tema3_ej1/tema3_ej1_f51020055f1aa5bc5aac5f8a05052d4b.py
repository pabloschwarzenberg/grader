# completa el código de la función
def suma_divisores(a):
    suma_divisor = 0
    primo = 0 
    for numero in range(1, a):
        if a % numero == 0:
            suma_divisor = suma_divisor + numero
    if suma_divisor == 1:
       primo=1
    else: 
       primo=0
    return (suma_divisor,primo)