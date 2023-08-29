import math

def area_triangulo(base,altura):
    resultado=((base*altura)/2)
    return resultado

def area_rectangulo(lado1,lado2):
    resultado2=(lado1*lado2)
    return resultado2

def area_rombo(diagonal1,diagonal2):
    resultado3=((diagonal1*diagonal2)/2)
    return resultado3

def area_circulo(r):
    resultado4=(math.pi*r**2)
    return resultado4
               
a1=area_triangulo(3,4)
print(a1)
a2=area_rectangulo(3,4)
print(a2)
a3=area_rombo(3,4)
print(a3)
a4=area_circulo(4)
print(a4)
           