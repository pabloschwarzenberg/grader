import math
def area_triangulo(base,altura):
    areaT = (base*altura)/2
    return areaT
    pass

def area_rectangulo(base,altura):
    areaR = base*altura
    return areaR
    pass

def area_rombo(diagonal1,diagonal2):
    areaRo = (diagonal1 * diagonal2)/2
    return areaRo
    pass

def area_circulo(radio):
    areaC =  math.pi * radio**2
    return areaC
    pass

if __name__ == "__main__":
    pass
           