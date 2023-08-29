from math import pi
def area_triangulo(base,altura):
 a_area = base * altura
 area = a_area/2
 return area 

def area_rectangulo(base,altura):
  area = base*altura
  return area

def area_rombo(diagonal1,diagonal2):
 a_area = diagonal1* diagonal2
 area = a_area/2
 return area

def area_circulo(radio):
 area = pi* radio**2
 return area

