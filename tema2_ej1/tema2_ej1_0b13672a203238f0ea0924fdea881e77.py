import math

def area_triangulo(base,altura):
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
   area = base*altura
   return area 
   
def area_rombo(diagonal1,diagonal2):
   area = diagonal1*diagonal2/2
   return area
   
def area_circulo(radio):
   rad = math.pi
   area = (radio**2)*rad
   return area

