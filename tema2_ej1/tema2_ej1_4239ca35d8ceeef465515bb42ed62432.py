def area_triangulo(base,altura):
  area=(base*altura)/2
  return area

def area_rectangulo(base,altura):
  area=(base*altura)
  return area
def area_rombo(diagonal1,diagonal2):
  area=(diagonal1*diagonal2)/2
  return area

def area_circulo(radio):
  import math
  area= math.pi * radio**2
  return area

  altura=int(input("ingrese altura"))
  base=int(input("ingrese base"))
  diagonal1=int(input("ingrese diagonal1"))
  diagonal2=int(input("ingrese diagonal2"))
  radio=int(input("ingrese radio"))
  print(area_circulo(radio))
  print(area_rectangulo(base,altura))
  print(area_rombo(diagonal1,diagonal2))
  print(area_triangulo(base,altura))