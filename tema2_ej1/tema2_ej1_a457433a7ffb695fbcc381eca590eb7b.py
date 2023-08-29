from math import pi

def area_rectangulo(lado1,lado2):
    return lado1*lado2
def area_circulo(radio):
    return pi*radio**2
def area_triangulo(base,altura):
    return (base*altura)/2
def area_rombo(Diagonalmayor,diagonalmenor):
    return (Diagonalmayor*diagonalmenor)/2

print(area_rectangulo(5,7))
print(area_circulo(5))
print(area_triangulo(6,9))
print(area_rombo(5,3))
           