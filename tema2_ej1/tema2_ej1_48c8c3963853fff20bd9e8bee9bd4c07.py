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
  area=(radio**2)*(math.pi)
  return area

if __name__ == "__main__":
  print("(1) Area de un triangulo.")  
  print("(2) Area de un rectangulo.")  
  print("(3) Area de un rombo.")  
  print("(4) Area de un circulo.")  
  opcion=int(input("Elige que quieres calcular: "))

  if opcion==1:
    altura1=float(input("Ingrese la altura del triangulo: "))
    base1=float(input("Ingrese la base del triangulo: "))
    print("El area del triangulo es:")
    area_triangulo(base1,altura1)

  if opcion==2:
    altura2=float(input("Ingrese la altura del rectangulo: "))
    base2=float(input("Ingrese la base del rectangulo: "))
    print("El area del rectangulo es:")
    area_rectangulo(base2,altura2)

  if opcion==3:
    diagonal1=float(input("Ingrese la medida de la diagonal 1: "))
    diagonal2=float(input("Ingrese la medida de la diagonal 2: "))
    print("El area del rombo es:")
    area_rombo(diagonal1,diagonal2)

  if opcion==4:
    radio=float(input("Ingrese la medida del radio del circulo: "))
    print("El area del circulo es:")
    area_circulo(radio)