import math
def area_triangulo(base,altura):
    a=float(altura)
    b=float(base)
    area=a*b/2
    return area
    pass

def area_rectangulo(base,altura):
    a=float(altura)
    b=float(base)
    area=a*b
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    d1=float(diagonal1)
    d2=float(diagonal2)
    area=d1*d2/2
    return area
    pass

def area_circulo(radio):
    r=float(radio)
    area=math.pi*radio*radio
    return area
    pass
           