import math
def area_triangulo(base,altura):
    triangulo=base*altura/2
    return triangulo
    
def area_rectangulo(base,altura):
    rectangulo=base*altura
    return rectangulo

def area_rombo(diagonal1,diagonal2):
    rombo=diagonal1*diagonal2/2
    return rombo

def area_circulo(radio):
    circulo=math.pi*radio**2
    return circulo

if __name__ == "__main__":
    pass
           