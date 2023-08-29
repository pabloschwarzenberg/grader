#import math

def area_triangulo(base,altura):
  area_pas1 = base * altura
  area_pas2 = area_pas1 / 2
  return area_pas2

def area_rectangulo(base,altura):
  area_pas1 = base * altura
  return area_pas1

def area_rombo(diagonal1,diagonal2):
    area1 = diagonal1 * diagonal2
    area = area1 / 2
    return area

def area_circulo(radio):
  import math
  rad1 = radio ** 2
  area = math.pi * rad1
  return area

if __name__ == "__main__":
    pass
           