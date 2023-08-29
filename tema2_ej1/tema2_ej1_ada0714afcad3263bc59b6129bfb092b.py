from math import pi
def area_triangulo(base,altura):
  ar = base*altura/2
  return ar 



def area_rectangulo(base,altura):
  ar = base*altura
  return ar
 

def area_circulo(radio):
  ar = pi * radio ** 2 
  return ar
 

def area_rombo(diagonal1,diagonal2):
  ar = diagonal1 * diagonal2 / 2 
  return ar