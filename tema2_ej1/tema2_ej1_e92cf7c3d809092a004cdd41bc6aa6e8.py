import math
def area_triangulo(b,h):
    area=(b*h)/2
    return print('El area del triángulo es: ', area)

def area_rectangulo(b,h):
    area=b*h
    return print('El area del Rectángulo es: ', area)

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1 * diagonal2)/2
    return print('El area del Rombo es: ', area)

def area_circulo(R):
    area=math.pi*R**2
    return print('el area del circulo es %.3f ' % area)
