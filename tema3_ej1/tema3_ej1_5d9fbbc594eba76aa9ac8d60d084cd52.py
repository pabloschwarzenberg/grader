# completa el código de la función
def suma_divisores(a):
    n = 1
    suma = 0
    while n < a:
        y = a%n
        if y == 0:
            suma+=n
        n+=1
    if suma == 1:
        return suma,True
    else:
        return suma,False