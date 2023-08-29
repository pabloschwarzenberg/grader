# completa el código de la función
def suma_divisores(a):
    lista = []
    suma_div = 0
    for i in range(1,a):
        if a % i == 0:
           lista.append(i)
    for k in lista:
        suma_div = suma_div + k
    if suma_div == 1:
       return (suma_div,True)
    else:
      return (suma_div,False)
           