def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
import math
def area_triangulo(base,altura):
    area = base * altura/2
    return area
def area_rectangulo(base,altura):
    area = base * altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area = math.pi*radio**2
    return area