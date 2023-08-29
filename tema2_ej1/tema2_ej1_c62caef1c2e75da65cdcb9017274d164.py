from math import pi
def area_triangulo(base,altura):
  a = base*altura/2
  return a 



def area_rectangulo(base,altura):
  a = base*altura
  return a
 

def area_circulo(radio):
  a = pi * radio ** 2 
  return a
 

def area_rombo(diagonal1,diagonal2):
  a = diagonal1 * diagonal2 / 2 
  return a
def suma_divisores(A):
  divisores = [0]
  for i in range(1, A): 
    if A % i == 0: 
      divisores.append(i)





  return sum(divisores), "True"

final = suma_divisores(13) 
print(final)
           