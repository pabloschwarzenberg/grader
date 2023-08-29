from math import pi
def area_triangulo(base,altura):
  a=(base*altura)/2
  return (a)
def area_rectangulo(base,altura):
  a=(base*altura)
  return (a)
def area_rombo(diagonal1,diagonal2):
  a=(diagonal1*diagonal2)/2
  return (a)
def area_circulo(radio):
  a=(pi*radio**2)
  return (a)
  
  eleccion=int(input("1: area del triangulo, 2: area del rectangulo, 3: area del rombo, 4: area del circulo o ingrese 0 para salir:"))

  if eleccion==0:
    print("Adiós")
    
  if eleccion==1:
    base=eval(input("Ingrese la base:"))
    altura=eval(input("Ingrese la altura:"))
    print(area_triangulo(base,altura))
    
  if eleccion==2:
    base=eval(input("Ingrese la base:"))
    altura=eval(input("Ingrese la altura:"))
    print(area_rectangulo(base,altura))

  if eleccion==3:
    diagonal1=eval(input("Ingrese primera diagonal:"))
    diagonal2=eval(input("Ingrese segunda diagonal:"))
    print(area_rombo(diagonal1,diagonal2))
    
  if eleccion==4:
    radio=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(radio))