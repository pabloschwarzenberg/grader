import math

def area_triangulo(base,altura):
    AREA=base*altura/2
    figura= 'Triangulo'
    print('El area del',figura,'es',AREA)
    return AREA

def area_rectangulo(base,altura):
    AREA=base*altura
    figura= 'Rectangulo'
    print('El area del',figura,'es',AREA)
    return AREA

def area_rombo(diagonal1,diagonal2):
    AREA=diagonal1*diagonal2/2
    figura= 'Rombo'
    print('El area del',figura,'es',AREA)
    return AREA

def area_circulo(radio):
    AREA=math.pi*radio*radio
    figura= 'Circulo'
    print('El area del',figura,'es',AREA)
    return AREA
     