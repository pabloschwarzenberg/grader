import math
def area_triangulo(base,altura):
    area=base*altura/2
    print(area)
    return area

def area_rectangulo(base,altura):
    area=base*altura
    print(area)
    return area

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    print(area)
    return area

def area_circulo(radio):
    area=radio**2*math.pi
    return area


           