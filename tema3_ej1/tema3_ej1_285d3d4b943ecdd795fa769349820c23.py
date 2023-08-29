# completa el código de la función
def suma_divisores(a):
    divisor = []
    nprimo = False
    for i in range(1,a):
      if a % i == 0:
        divisor.append(i)
    suma = sum(divisor)
    for n in range(2,suma):
        if suma % n ==0:
          nprimo= True
    if suma == 1:
        nprimo = True
    
    return suma , nprimo           