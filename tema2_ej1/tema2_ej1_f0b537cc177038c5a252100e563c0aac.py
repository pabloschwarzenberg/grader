import math 

def area_triangulo(b,al):
    a = b*al/2
    return a
    pass

def area_rectangulo(b,al):
    a = b*al
    return a
    pass

def area_rombo(diagonal1,diagonal2):
    a = diagonal1*diagonal2/2
    return a
    pass

def area_circulo(radio):
    a = float(math.pi*radio*radio)
    return a
    pass
           