# completa el código de la función
def suma_divisores(a):
    divisores=[]
    divisor=1
    suma = 0
    while a > divisor:
          if a%divisor == 0:
             divisores.append(divisor)
          divisor += 1
    for i in divisores:
        suma += i
    if suma == 1:
        return suma,True
    return suma,False
 