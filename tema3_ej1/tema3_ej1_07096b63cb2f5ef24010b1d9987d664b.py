# completa el código de la función
def suma_divisores(x,y):
    global numero
    suma_divisores = x % y
    divisor = numero
    while divisor > 1:
        divisor = divisor - 1
        if (numero % divisor) == 0:
            numero += divisor
    return suma_divisores(x,y)        

    

numero = 20
sum = 0
acum = 0
for i in range(1, numero):
    if (suma_divisores(numero,i)) == 0:
        sum = sum + i
    else:
        pass
print("SUMA DIVISOR", sum)

