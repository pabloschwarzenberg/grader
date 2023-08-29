# completa el código de la función
"""
def suma_divisores(numero):
    suma =0
    for i in range(1,numero):
        if numero%i==0:
            suma+=i
    if suma ==1:
        return suma,True
    else:
        return suma,False
"""
def suma_divisores(a):
    divisores = []
    for i in range(1, a + 1):
      if a % i == 0 and a != i:
         divisores.append(i)
    if sum(divisores) == 1:
      return sum(divisores), True
    else:
      return sum(divisores), False
    return sum(divisores)