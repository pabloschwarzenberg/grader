def area_triangulo(base,altura):
    result = base * altura / 2
    return result

def area_rectangulo(base,altura):
    result = base * altura
    return result

def area_rombo(diagonal1,diagonal2):
    result = (diagonal1 * diagonal2)/2
    return result

def area_circulo(radio):
    from math import pi
    result = radio**2 * pi
    return result

           