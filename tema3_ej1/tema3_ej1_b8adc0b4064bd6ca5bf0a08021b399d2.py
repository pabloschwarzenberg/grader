# completa el código de la función
'''
def suma_divisores(a):
    divisores = [0]
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
    return sum(divisores), sum(divisores)==1
'''
def suma_divisores(a):
  divisores = [] #Para el número 1, tu función debiera retornar (0, False)
  for i in range(1, a): #sin incluir al número
    if a % i == 0:
      divisores.append(i)
  resultado = sum(divisores) # suma de los divisores de a
  if resultado == 1: # si la suma de sus divisores es 1, el número es primo.
    return resultado, True
  else:
    return resultado, False

           