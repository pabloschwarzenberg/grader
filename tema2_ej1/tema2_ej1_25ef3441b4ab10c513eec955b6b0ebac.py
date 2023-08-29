from math import *

#----------------------------------------------
def area_rectangulo(base,altura):
    area=base*altura
    return area
#----------------------------------------------
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
#----------------------------------------------
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
#----------------------------------------------
def area_circulo(r):
    area=pi*r*r
    return area
#----------------------------------------------
if __name__ == "__main__":
  pass
  opcion=int(input("Ingrese la opcion de la figura a la que quiere calcular el area: (1:Rectangulo, 2:Triangulo, 3:Rombo, 4: Circulo)"))
  if opcion==1:
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
    area=area_rectangulo(base,altura)
    print("El area de la figura es:",area)
  if opcion==2:
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
    area=area_triangulo(base,altura)
    print("El area de la figura es:",area)
  if opcion==3:
    diagonal1=int(input("Ingrese la diagonal1: "))
    diagonal2=int(input("Ingrese la diagonal2: "))
    area=area_rombo(diagonal1,diagonal2)
    print("El area de la figura es:",area)
  if opcion==4:
    radio=int(input("Ingrese el radio: "))
    area=area_circulo(radio)
    print("El area de la figura es:",area)
