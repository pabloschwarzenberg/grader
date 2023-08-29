def area_triangulo(base,altura):
    area1=base*altura/2
    return area1

def area_rectangulo(base,altura):
    area2=base*altura
    return area2

def area_rombo(diagonal1,diagonal2):
    area3=diagonal1*diagonal2/2
    return area3

def area_circulo(radio):
    import math
    area4=math.pi*(radio**2)
    return area4

def menu(area_escoger):
  menu= """
  [1] Area Triangulo
  [2] Area Rectangulo
  [3] Area Rombo
  [4] Area Circulo
  """
  print(menu)
  area_escoger=int(input("Seleccione Area: "))
  while (area_escoger<4 or area_escoger>1):
    area_escoger=int(input("Seleccione Area: "))
    if area_escoger==1:
      base=int(input("b "))
      altura=int(input("a "))
      print(area_triangulo(base,altura))
      break
    elif area_escoger==2:
      base=int(input("b "))
      altura=int(input("a "))
      print(area_rectangulo(base,altura))
      break
    elif area_escoger==3:
      diagonal1=int(input("d1 "))
      diagonal2=int(input("d2 "))
      print(area_rombo(diagonal1,diagonal2))
      break
    if area_escoger==4:
      radio=int(input("r "))
      print(area_circulo(radio))
      break