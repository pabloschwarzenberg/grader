# completa el código de la función
def suma_divisores(a):
    acum = 0
    for i in range(1,a):
        if a % i == 0:
           acum += i
    if acum == 1:
       return acum,True
    else:
      return acum,False
           