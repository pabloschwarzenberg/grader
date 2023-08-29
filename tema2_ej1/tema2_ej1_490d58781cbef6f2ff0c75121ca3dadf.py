def area_triangulo(base,altura):
  area_triangulo=(base*altura)/2
  return area_triangulo
def area_rectangulo(base,altura):
  area_rectangulo=base*altura
  return area_rectangulo
def area_rombo(diagonal1,diagonal2):
  area_rombo=(diagonal1*diagonal2)/2
  return area_rombo
def area_circulo(radio):
  import math
  math.pi
  area_circulo=math.pi*(radio**2)
  return area_circulo
figura=["triangulo","rectangulo","rombo","circulo"]
if figura=="triangulo":
  print(area_triangulo(radio))
elif figura=="rectangulo":
  print(area_rectangulo(base,altura))  
elif figura=="rombo":
  print(area_rombo(diagonal1,diagonal2))  
elif figura=="circulo":
  print(area_circulo(radio))  
  
