from math import pi
def area_triangulo(base,altura):
  area = base*altura/2
  return area 



def area_rectangulo(base,altura):
  area = base*altura
  return area
 

def area_circulo(radio):
  area = pi * radio ** 2 
  return area
 

def area_rombo(diagonal1,diagonal2):
  area = diagonal1 * diagonal2 / 2 
  return area
def suma_divisores(a):
  divisores = [0]
  for i in range(1, a): 
    if a % i == 0: 
      divisores.append(i)





  return sum(divisores), "True"

final = suma_divisores(13) 
print(final)