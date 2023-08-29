import math
def area_triangulo(base,altura):
    area = (float(base)*float(altura))/ 2
    return area
    pass
def area_rectangulo(base,altura):
    area = float(base)*float(altura)
    return area
    pass
def area_rombo(diagonal1,diagonal2):
    area = (float(diagonal1)*float(diagonal2))/2
    return area
    pass
def area_circulo(radio):
    area = math.pi*(float(radio)**2)
    return area
    pass

