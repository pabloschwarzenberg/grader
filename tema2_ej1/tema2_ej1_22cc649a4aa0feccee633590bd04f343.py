import math

def area_triangulo(b,a):
    area=b*a/2
    return print("El area del triangulo es: ", area)

def area_rectangulo(b,a):
    area=b*a
    return print("El area del rectangulo es: ", area)

def area_rombo(d1,d2):
    area=d1*d2/2
    return print("El area del rombo es: ", area)

def area_circulo(r):
    area=math.pi*r**2
    return print("El area del circulo es: ", area)
           