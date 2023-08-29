import math

def area_triangulo(base,altura):
    area=base*altura/2
    return(area)
    pass

def area_rectangulo(base,altura):
    area=base*altura
    return(area)
    pass

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return(area)
    pass

def area_circulo(radio):
    area=math.pi*(radio**2)
    return(area)
    pass
           