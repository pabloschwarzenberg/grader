def area_triangulo(base,altura):
    area_triangulo = (base * altura)/2
    return area_triangulo

def area_rectangulo(base,altura):
    area_retangulo = base * altura
    return area_retangulo

def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1 * diagonal2)/2
    return area_rombo

def area_circulo(radio):
    from math import pi
    r = pow(radio,2)
    area_circulo = pi*(r)
    return area_circulo
           