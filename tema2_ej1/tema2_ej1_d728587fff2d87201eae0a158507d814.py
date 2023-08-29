import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=math.pi*radio**2
    return area
if __name__ == "__main__":
  
  opcion=int(input("Ingrese un valor: "))
  if opcion==1:
     base=int(input("Ingrese base: "))
     altura=int(input("Ingrese altura: "))
     print(area_triangulo(base,altura))
 
  if opcion==2:
     base=int(input("Ingrese base: "))
     altura=int(input("Ingrese altura: "))
     print(area_rectangulo(base,altura))

  if opcion==3:
     diagonal1=int(input("Ingrese la diagonal: "))
     diagonal2=int(input("Ingrese la otra diagonal: "))
     print(area_rombo(diagonal1,diagonal2))
     
  if opcion==4:
     radio=int(input("Ingrese radio: "))
     print(area_circulo(radio))