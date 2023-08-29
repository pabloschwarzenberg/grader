import math
pi=math.pi
def area_triangulo(base,altura):
    total=(base*altura)/2
    return total

def area_rectangulo(base,altura):
    total=float(base*altura)
    return total

def area_rombo(diagonal1,diagonal2):
    total=(diagonal1*diagonal2)/2
    return total

def area_circulo(radio):
    total=pi*radio**2
    return total
