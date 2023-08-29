import math
def area_triangulo(base,altura):
    x = (base * altura)/2
    return x

def area_rectangulo(base,altura):
    a = (base * altura)
    return a

def area_rombo(diagonal1,diagonal2):
    b = diagonal1 * diagonal2 / 2
    return b

def area_circulo(radio):
    z = math.pi * radio**2
    return z


if __name__ == "__main__":
    pass 