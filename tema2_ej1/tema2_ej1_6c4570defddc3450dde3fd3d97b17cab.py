from math import pi

opcion = ("Ingrese 1 para area triangulo, 2 para area de rectangulo, 3 para area de rombo, 4 para area de circulo ")

def area_triangulo(base,altura):
 area = (base * altura)/2
 return (area)

def area_rectangulo(base,altura):
  area = (base * altura)
  return (area)

def area_rombo(diagonal1,diagonal2):
  area = (diagonal1 * diagonal2)/2
  return (area)
    
def area_circulo(radio):
  area = (pi * radio **2)
  return (area)
           