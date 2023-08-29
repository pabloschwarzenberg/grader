import math
def area_triangulo(base,altura):
  area = (base*altura)/2
  return area

def area_rectangulo(base,altura):
  area = base*altura
  return area

def area_rombo(D1,D2):
  area = (D1*D2)/2
  return area

def area_circulo(radio):
  area = (radio**2)*math.pi
  return area