import math


def area_triangulo(base,altura):
    total = base * altura/2
    return total
    pass

def area_rectangulo(base,altura):
    total = base * altura
    return total
    pass

def area_rombo(diagonal1,diagonal2):
    total = diagonal1 * diagonal2/2
    return total
    pass

def area_circulo(radio):
    total = math.pi * (radio**2)
    return total
    pass

if __name__ == "__main__":
    pass
           