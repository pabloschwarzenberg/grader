input('que es lo que desea calcular?:, (rectangulo), (triangulo), (rombo), (circulo)')
a = ('rectangulo')
def area_rectangulo(base,altura):
    area = base * altura
    return area
print('el area del rectangulo es'), print(area_rectangulo(2,3))
b = ('triangulo')
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area
print('el area del triangulo es'),print(area_triangulo(3,6))
c = ('rombo')
def area_rombo(dmenor,dmayor):
    area = (dmenor*dmayor)/2
    return area
print('el area del rombo es'),print(area_rombo(4,7))
d = ('circulo')
from math import pi
def area_circulo(r):
    area = (pi * r**2)
    return area
print('el area del circulo es'),print(area_circulo(2))
           