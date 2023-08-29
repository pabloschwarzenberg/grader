import math
def area_triangulo(base,altura):
    a = base * altura * 1/2
    return a

def area_rectangulo(base,altura):
    a = base * altura
    return a

def area_rombo(diagonal1,diagonal2):
    a = diagonal1 * diagonal2 * 1/2
    return a

def area_circulo(radio):
    pi = math.pi
    a = pi * radio**2
    return a

if __name__ == "__main__":
    pass
           