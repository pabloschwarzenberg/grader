def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
    def area_triangulo(base, altura):
    return base*altura/2
if _name_ == "_main_":
  a=float(input('Ingrese la altura del triangulo en metros: '))
  b= float(input('Ingrese la base del triangulo en metros: '))
  print(area_triangulo(base=b,altura=a))
pass
def area_rectangulo(base, altura):
    return base*altura
if _name_ == "_main_":
  a=float(input('Ingrese la altura rectangulo del en metros: '))
  b= float(input('Ingrese la base del rectangulo en metros: '))
  print(area_rectangulo(base=b,altura=a))
pass
def area_rombo(diagonal1, diagonal2):
    return diagonal1*diagonal2/2
if _name_ == "_main_":
  a=float(input('Ingrese el diagonal1 del rombo en metros: ')) 
  b= float(input('Ingrese el diagonal2 del rombo en metros: '))
  print(area_rombo(diagonal1=b,diagonal2=a))
pass
import math 
def area_circulo(radio):
    return math.pi*(radio**2)
if _name_ == "_main_":
  r =float(input('Ingrese el radio en metros: '))
  print(area(radio=r))
pass       