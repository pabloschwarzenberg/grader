from math import pi

def area_triangulo(base,altura):
    area_triangle = (altura * base) / 2
    return area_triangle

def area_rectangulo(base,altura):
    area_rectangle = base * altura
    return area_rectangle

def area_rombo(diagonal1,diagonal2):
    area_rombo = (diagonal1 * diagonal2) / 2
    return area_rombo

def area_circulo(radio):
    area_circle = pi * (radio ** 2)
    return area_circle

if __name__ == "__main__":
    pass
           