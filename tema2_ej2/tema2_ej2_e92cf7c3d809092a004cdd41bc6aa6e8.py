# completa el código de la función
def amigos (a,b):
    valor1 = 1
    valor2 = 1
    for i in range(2,a):
        if (a % i == 0):
            valor1 = valor1 + i
            
    for x in range(2,b):
        if (b % x == 0):
            valor2 = valor2 + x
            
    if valor1 == b and valor2 == a:
        return (True)
    else:
        return (False)