import math
def area_triangulo(base,altura):
    global a
    a=(base*altura)/2
    a=float(a)
    return a
    
def area_rectangulo(base,altura):
    global a
    a=base*altura
    return a
    

def area_rombo(diagonal1,diagonal2):
    global a
    a=(diagonal1*diagonal2)/2
    return a

def area_circulo(radio):
    global a
    a=(math.pi)*(radio**2)
    return a
    

if __name__ == "__main__":
  f=input("area de que figura desea calcular? ")
  if f=="triangulo":
    base=input("ingrese el valor de la base: ")
    base=float(base)
    altura=input("ingrese el valor de la altura: ")
    altura=float(altura)
    area=area_triangulo(base,altura)
  if f=="rectangulo":
    base=input("ingrese el valor del lado (base): ")
    base=float(base)
    altura=input("ingrese el valor del lado (altura): ")
    altura=float(altura)
    area=area_rectangulo(base,altura)
  if f=="circulo":
    radio=input("ingrese el valor del radio: ")
    radio=float(radio)
    area=area_circulo(radio)
  if f=="rombo":
    diagonal1=input("ingrese el valor de la digonal 1: ")
    diagonal1=float(diagonal1)
    diagonal2=input("ingrese el valor de la digonal 2: ")
    diagonal2=float(diagonal2)
    area_rombo(diagonal1,diagonal2)
           