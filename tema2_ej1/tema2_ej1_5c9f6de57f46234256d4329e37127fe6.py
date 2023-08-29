from math import pi
def area_triangulo(base,altura):
  area_t=(base*altura)/2
  return area_t
  
def area_rectangulo(base,altura):
  area_re=base*altura
  return area_re

def area_rombo(diagonal1,diagonal2):
  area_ro=(diagonal1*diagonal2)/2
  return area_ro

def area_circulo(radio):
  area_c=pi*(radio**2)
  return area_c
  
