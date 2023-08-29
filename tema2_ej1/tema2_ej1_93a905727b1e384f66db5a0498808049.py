import math

def area_triangulo(base,altura):
    area = (base * altura)/2
    return area
    pass
    
def area_rectangulo(base,altura):
    area = base * altura
    return area
    pass
    
def area_rombo(diagonal,diagonal2):
    area = (diagonal * diagonal2)/2
    return area
    pass
    
def area_circulo(R):
   area=math.pi*R**2
   return area
   pass