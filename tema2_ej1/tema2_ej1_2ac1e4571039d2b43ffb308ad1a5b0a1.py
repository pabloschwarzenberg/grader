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
  print("Menu")
  option=int(input("Ingresar 1 para area triangulo, 2 para area de rectangulo, 3 para del rombo, 4 para area de circulo o 0 para salir:"))
  while(option==0):
    print("Hasta la proxima")
    break
  while(option==1):
    base=float(input("Ingrese la base:"))
    altura=float(input("Ingrese la altura:"))
    print(area_triangulo(base,altura))
    break
  while(option==2):
    base=float(input("Ingresar base:"))
    altura=float(input("Ingresar altura:"))
    print(area_rectangulo(base,altura))
    break
  while(option==3):
    diagonalol=float(input("Ingresar 1ra diagonal:"))
    diagonalolo=float(input("Ingresar 2da diagonal:"))
    print(area_rombo(diagonalol,diagonalolo))
    break
  while(option==4):
    radio=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(radio))
    break