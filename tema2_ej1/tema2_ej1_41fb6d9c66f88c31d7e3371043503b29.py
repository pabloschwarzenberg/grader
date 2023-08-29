import math
def area_triangulo(base,altura):
    area = (1/2)*base*altura
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (1/2) * diagonal1* diagonal2
    return area

def area_circulo(radio):
    area = float(math.pi * (radio**2))
    return area

if __name__ == "__main__":
    pass
           