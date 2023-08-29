import math
def area_triangulo(base,altura):
    b=base
    a=altura
    area=0.5*a*b
    return area
    pass

def area_rectangulo(base,altura):
    b=base
    a=altura
    return a*b
    pass

def area_rombo(diagonal1,diagonal2):
    b= diagonal1
    a=diagonal2
    return a*b/2
    pass

def area_circulo(radio):
    r=radio
    return (r**2)*(math.pi)
    pass
           