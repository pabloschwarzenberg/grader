import math
def area_triangulo(base,altura):
  areaT = base*altura/2
  return areaT

def area_rectangulo(base,altura):
  areaR = base*altura
  return areaR
def area_rombo(diagonal1,diagonal2):
  areaRO  = diagonal1*diagonal2/2
  return areaRO

def area_circulo(radio):
  areaC = math.pi*radio**2
  return areaC
           