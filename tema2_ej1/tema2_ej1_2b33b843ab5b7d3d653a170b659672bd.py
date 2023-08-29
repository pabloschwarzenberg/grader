import math
def area_triangulo(base,altura):
    area_del_triangulo = base*altura/2
    return  area_del_triangulo

def area_rectangulo(base,altura):
    area_del_rectangulo=base*altura
    return area_del_rectangulo

def area_rombo(diagonal1,diagonal2):
    area_del_rombo= diagonal1*diagonal2/2
    return area_del_rombo
def area_circulo(radio):
    area_del_circulo=math.pi*(radio**2)
    return  area_del_circulo