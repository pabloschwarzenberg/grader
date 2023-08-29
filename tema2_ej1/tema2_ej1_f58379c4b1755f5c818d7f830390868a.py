def area_triangulo(base,altura):
    at = base * altura / 2
    return at

def area_rectangulo(base,altura):
    are = base * altura
    return are

def area_rombo(diagonal1,diagonal2):
    aro = diagonal1 * diagonal2 / 2
    return aro

def area_circulo(radio):
    import math
    ac = math.pi * (radio**2)
    return ac  
    