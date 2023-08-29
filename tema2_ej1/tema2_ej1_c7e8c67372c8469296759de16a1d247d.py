import math
def area_triangulo(base,altura):
 area_tri=(base * altura)/2
 return area_tri

def area_rectangulo(base,altura):
 area_rec = base*altura
 return area_rec
def area_rombo(diagonal1,diagonal2):
 area_rom = (diagonal1 * diagonal2)/ 2
 return area_rom
def area_circulo(radio):
  area_cir = (radio * radio) * math.pi
  return area_cir
if __name__ == "main":
 while True:
  opcion = int(input("(0)salir - (1)triangulo - (2)rectangulo - (3)rombo - (4)circulo"))
  if opcion == 1:
   base = int(input("ingrese el base"))
   altura = int(input("ingrese la altura"))
   area = area_triangulo(base, altura)
   print(area)
  if opcion == 2:
   base = int(input("ingrese el base"))
   altura = int(input("ingrese la altura"))
   area = area_rectangulo(base, altura)
   print(area)
  if opcion == 3:
   d1 = int(input("ingrese la diagonal 1"))
   d2 = int(input("ingrese la diagonal 2"))
   area = area_rombo(d1, d2)
   print(area)
  if opcion == 4:
   radio = int(input("ingrese el radio"))
   area = area_circulo(radio)
   print(area)
  if opcion == 0:
   False  