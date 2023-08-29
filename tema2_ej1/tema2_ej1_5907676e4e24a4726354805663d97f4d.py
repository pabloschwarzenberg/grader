from math import pi


def area_traingulo(base,altura):
    print(base * altura)
    area_traingulo(base,altura)
    pass

def area_rectangulo(base,altura):
    print(base * altura)
    pass

def area_rombo(diagonal1,diagonal2):
    print(diagonal1 * diagonal2 / 2)
    pass
    
def area_circulo(radio):
    print(radio**2 * pi)
    pass