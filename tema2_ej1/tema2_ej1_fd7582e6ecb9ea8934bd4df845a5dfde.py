import math 
π=3.141592653589793115997963468544
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=(base*altura)
    return area
def area_rombo(diagonal1,diagonal2):
    if (diagonal1>diagonal2):
        area=(diagonal1*diagonal2)/2
    else:
        area=(diagonal2*diagonal1)/2
    return area
def area_circulo(radio):
    area=π*radio**2
    return area
        