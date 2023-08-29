import math
def area_triangulo(base,altura):
  b = float(base)
  h = float(altura)
  aT = (b * h) / 2
  return aT

def area_rectangulo(base,altura):
  b = float(base)
  a = float(altura)
  aRe = b * a
  return aRe

def area_rombo(diagonal1,diagonal2):
  d1 = float(diagonal1)
  d2 = float(diagonal2)
  aRo = (d1 * d2) / 2
  return aRo

def area_circulo(radio):
  r = radio
  pi = math.pi
  aC= pi * (r ** 2)
  return aC
 