from math import pi
def area_triangulo(base,altura):
    at = (base*altura)/2
    return at

def area_rectangulo(base,altura):
    ar = base * altura
    return ar
    pass

def area_rombo(diagonal1,diagonal2):
    ar = (diagonal1 * diagonal2) /2
    return ar
    pass

def area_circulo(radio):
    ac = pi*(radio**2)
    return ac
    pass

if __name__ == "__main__":
    pass