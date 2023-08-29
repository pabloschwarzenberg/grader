import math
from math import pi
def area_triangulo(base, altura):
    area = (base*altura)/2
    return 
    pass
def area_rectangulo(base, altura):
    area = base * altura
    return 
    pass
def area_rombo(diagonal_mayor, diagonal_menor):
    area = diagonal_mayor*diagonal_menor/2
    return 
    pass
def area_circulo(radio):
    area = math.pi*radio**2
    return 
    pass 
    
if x == 1:
    base = int(input('Ingrese la base: '))
    altura = int(input('Ingrese la altura: '))
    area_triangulo(base, altura)

if x == 2:
    base = int(input('Ingrese la base: '))
    altura = int(input('Ingrese la altura: '))
    area_rectangulo(base, altura)

if x == 3:
    diagonal_mayor = int(input('Ingrese el valor de la diagonal mayor: '))
    diagonal_menor = int(input('Ingrese el valor de la diagonal menor: '))
    area_rombo(diagonal_mayor, diagonal_menor)

if x == 4:
    radio = int(input('Ingrese el radio del circulo: '))
    area_circulo(radio) 
    
if __name__ == "__main__":    
    x = int(input('Escoja una figura: '))    