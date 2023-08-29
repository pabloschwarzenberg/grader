#importaciones
import math
#area triangulo
def area_triangulo(b,h):
    area = b * h/2
    return area
#area rectangulo
def area_rectangulo(b,h):
    area = b * h
    return area
#area rombo
def area_rombo(d1,d2):
    area = (d1*d2)/2
    return area
#area de un circulo
def area_circulo(r):
    area = math.pi*r**2
    return area