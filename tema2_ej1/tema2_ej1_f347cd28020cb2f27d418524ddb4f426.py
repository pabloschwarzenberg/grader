import math
def area_triangulo(base,altura):
    area1=altura*base/2
    return area1
    
def area_rectangulo(base,altura):
    area2= base*altura
    return area2

def area_rombo(diagonal1,diagonal2):
    area3= diagonal1*diagonal2/2
    return area3

def area_circulo(radio):
    area4= radio**2*math.pi
    return area4
    
           