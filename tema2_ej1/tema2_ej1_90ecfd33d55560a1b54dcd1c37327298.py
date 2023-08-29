from math import pi
def area_triangulo(base,altura):
  area=(base*altura)/2
  return (area)
def area_rectangulo(base,altura):
  area=(base*altura)
  return (area)
def area_rombo(diagonal1,diagonal2):
  area=(diagonal1*diagonal2)/2
  return (area)
def area_circulo(radio):
  area=(pi*radio**2)
  return (area)
if __name__=="main":
  print("Menú")
  eleccion=int(input("Ingrese 1 para el área de un triangulo, 2 para el área de un rectángulo, 3 para área de un rombo o 4 para el área de un circulo: "))
  while(eleccion==1):
    base=float(input("Ingrese la base del triángulo: "))
    altura=float(input("Ingrese la altura del triángulo: "))
    print(area_triangulo(base,altura))
    break
  while(eleccion==2):
    base=float(input("Ingrese la base del rectángulo: "))
    altura=float(input("Ingrese la altura del rectángulo: "))
    print(area_rectangulo(base,altura))
    break
  while(eleccion==3):
    diagonal1=float(input("Ingrese primera diagonal del rombo: "))
    diagonal2=float(input("Ingrese segunda diagonal del rombo: "))
    print(area_rombo(diagonal1,diagonal2))
    break
  while(eleccion==4):
    radio=float(input("Ingrese el radio del circulo: "))
    print(area_circulo(radio))
    break