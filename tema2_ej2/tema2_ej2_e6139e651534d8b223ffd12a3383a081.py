def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma
def suma_divisores2(numerob):
    sumab = 0
    for x in range(1, numerob):
        if numerob % x == 0:
            sumab += x
    return sumab

def amigos (numero, numerob):
    if(suma_divisores(numero))== (numerob) and (suma_divisores(numerob))==(numero):
        return True
    else:
      return False 