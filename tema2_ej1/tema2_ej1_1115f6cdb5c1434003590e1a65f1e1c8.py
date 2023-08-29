import math

def area_triangulo(base,altura):
    return (base * altura)/2

def area_rectangulo(base,altura):
    return (base * altura)

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2)/2

def area_circulo(radio):
    pi = math.pi
    radio = pow(radio, 2)
    return pi*radio

if __name__ == "__main__":
    pass