def area_triangulo(base,altura):
    area_t=(base*altura)/2
    return area_t

def area_rectangulo(base,altura):
    area_r=base*altura
    return area_r

def area_rombo(diagonal1,diagonal2):
    area_ro=(diagonal1*diagonal2)/2
    return area_ro

def area_circulo(radio):
    import math
    area_c=math.pi*radio*radio
    return area_c