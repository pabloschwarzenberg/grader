import math as m
def area_triangulo(base,altura):
  area_triangulo= float(base * altura)/2
  return area_triangulo


def area_rectangulo(base,altura):
  area_rectangulo= float(base * altura)
  return area_rectangulo


def area_rombo(diagonal1,diagonal2):
  area_rombo= float(diagonal1 * diagonal2)/2
  return area_rombo


def area_circulo(radio):
  area_circulo= float(m.pi*(radio**2))
  return area_circulo