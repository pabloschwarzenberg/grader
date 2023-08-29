import math
def area_triangulo(base,altura):
    area= base * altura/2
    return print("El area del triángulo es:" , area)

    
def area_rectangulo(base,altura):
    area=base*altura
    return print('El area del rectangulo es: ', area)

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return print('El area del rombo es: ', area)

def area_circulo(radio):
    area=math.pi*radio**2
    return print('el area del circulo es %.3f ', area)           