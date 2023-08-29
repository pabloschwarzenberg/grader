import math
def area_triangulo(base,h):
    Area=(base*h)/2
    return Area

def area_rectangulo(base,h):
    Area=(base*h)
    return Area

def area_rombo(diagonal1,diagonal2):
    Area=(diagonal1*diagonal2)/2
    return Area

def area_circulo(radio):
    Area=(radio**2)*(math.pi)
    return Area
    
Todasareas=area_circulo,area_rombo,area_rectangulo,area_triangulo
           