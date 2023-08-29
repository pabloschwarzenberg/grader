import math
pi=math.pi
def area_triangulo(base,altura):
    areaTriang = (base*altura)/2
    return areaTriang
    pass

def area_rectangulo(base,altura):
    areaRectang = base*altura
    return areaRectang
    pass

def area_rombo(diagonal1,diagonal2):
    areaRomb = (diagonal1*diagonal2)/2
    return areaRomb
    pass

def area_circulo(radio):
  areaCirc = pi*(radio**2)
  return areaCirc
  pass