import math for pi

def area_circulo(radio):
    area=math.pi*radio**2
    return print('el area del circulo es "{0:.12f}".format(area))

def area_triangulo(base,altura):
    area=base*altura/2
    return print('El area del triángulo es "{0:.1f}".format(area))

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return print('El area del Rombo es"{0:.1f}".format(area)) ', area)

def area_rectangulo(base,altura):
    area=base*altura
    return print('El area del Rectángulo es"{0:.0f}".format(area))

