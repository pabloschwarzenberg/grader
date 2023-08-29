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
  print("MenÃº")
  opcion=int(input("Ingrese 1 para el area del triangulo, 2 para area del rectangulo, 3 para el area del rombo, 4 para area de circulo o ingrese 0 para salir:"))
  while(opcion==0):
    print("Hasta la proxima")
    break
  while(opcion==1):
    base=float(input("Ingrese la base:"))
    altura=float(input("Ingrese la altura:"))
    print(area_triangulo(base,altura))
    break
  while(opcion==2):
    base=float(input("Ingrese la base:"))
    altura=float(input("Ingrese la altura:"))
    print(area_rectangulo(base,altura))
    break
  while(opcion==3):
    diagonal1=float(input("Ingrese la primera diagonal, porfavor:"))
    diagonal2=float(input("Ingrese la segunda diagonal, porfavor:"))
    print(area_rombo(diagonal1,diagonal2))
    break
  while(opcion==4):
    radio=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(radio))
    break