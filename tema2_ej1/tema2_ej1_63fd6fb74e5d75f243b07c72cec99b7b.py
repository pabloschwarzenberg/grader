import math 

def area_triangulo(base,altura):
    areat = base * altura
    areat1 = areat/2
    return areat1

def area_rectangulo(base,altura):
    arear = base * altura
    return arear

def area_rombo(diagonal1,diagonal2):
    arearo = diagonal1*diagonal2
    arearo1  = arearo/2
    return arearo1

def area_circulo(radio):
    areac= math.pi * radio**2
    return areac


print(" el area de un circulo de radio 2 es", area_circulo(2))
print (" el area de un rectangulo de base 2 y altura 4 es", area_rectangulo(2,4))
print ("el area de un rombo de diagonal menor 4 y diagonal mayor 6 es: ", area_rombo(4,6))
print ("el area de un triangulo de base 3 y altura 4 es: ", area_triangulo(3,4))