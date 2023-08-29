from math import pi
def area_triangulo(base,altura):
    areatr = (base * altura)/2
    return areatr

def area_rectangulo(base,altura):
    areare = base* altura
    return areare

def area_rombo(diagonal1,diagonal2):
    arearo = (diagonal1 * diagonal2)/2
    return arearo
def area_circulo(radio):
    areaci = pi * (radio**2)
    return areaci
    
if __name__ == "__main__":
    pass
           