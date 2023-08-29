import math
def area_triangulo(base,alt):
    area = base * alt/2
    return area
    
def area_rectangulo(base,alt):
    area = base * alt
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = math.pi*radio**2
    return area
    