from math import pi
def area_triangulo(b,h):
  a=(b*h)/2
  return (a)
def area_rectangulo(b,h):
  a=(b*h)
  return (a)
def area_rombo(d1,d2):
  a=(d1*d2)/2
  return (a)
def area_circulo(r):
  a=(pi*r**2)
  return (a)
if __name__=="main":
  print("Menú")
  opc=int(input("Ingrese 1 para area triangulo, 2 para area de rectangulo, 3 para area de rombo, 4 para area de circulo o ingrese 0 para salir:"))
  while(opc==0):
    print("Hasta la proxima")
    break
  while(opc==1):
    b=float(input("Ingrese la base:"))
    h=float(input("Ingrese la altura:"))
    print(area_triangulo(b,h))
    break
  while(opc==2):
    b=float(input("Ingrese la base:"))
    h=float(input("Ingrese la altura:"))
    print(area_rectangulo(b,h))
    break
  while(opc==3):
    d1=float(input("Ingrese primera diagonal:"))
    d2=float(input("Ingrese segunda diagonal:"))
    print(area_rombo(d1,d2))
    break
  while(opc==4):
    r=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(r))
    break