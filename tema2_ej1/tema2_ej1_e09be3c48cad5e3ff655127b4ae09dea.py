import math
def area_triangulo(base, altura):
    return base * altura / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

print("Área de triángulo: ")
print(area_triangulo(2, 4))
           
           