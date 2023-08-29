# completa el código de la función
def suma_divisores(a):
    suma = 0
    for divisor in range(1,a+1):
       if a % divisor == 0:
           suma += divisor
    suma -= a
    if suma == 1:
        if a == 1:
          return (suma,False)
        else:
          return (suma,True)
    else:
        return (suma,False)
           