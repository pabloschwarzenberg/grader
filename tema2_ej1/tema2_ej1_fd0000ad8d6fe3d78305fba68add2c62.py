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

  opcion=int(input("1: area del triangulo, 2: area del rectangulo, 3: area del rombo, 4: area del circulo o ingrese 0 para salir:"))

  if opcion==0:
    print("Hasta la proxima")
    
  if opcion==1:
    base=eval(input("Ingrese la base:"))
    altura=eval(input("Ingrese la altura:"))
    print(area_triangulo(base,altura))
    
  if opcion==2:
    base=eval(input("Ingrese la base:"))
    altura=eval(input("Ingrese la altura:"))
    print(area_rectangulo(base,altura))

  if opcion==3:
    diagonal1=eval(input("Ingrese primera diagonal:"))
    diagonal2=eval(input("Ingrese segunda diagonal:"))
    print(area_rombo(diagonal1,diagonal2))
    
  if opcion==4:
    radio=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(radio))