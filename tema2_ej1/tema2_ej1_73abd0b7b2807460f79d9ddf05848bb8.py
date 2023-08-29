import math

def area_triangulo(base,altura):
    area= base*altura/2
    return area

print("el area del triangulo es",area_triangulo(11,7))
   
def area_rectangulo(base,altura):
    area= base*altura
    return area

print("el area del rectangulo es",area_rectangulo(10,6))

def area_rombo(diagonal1,diagonal2):
    area= diagonal1*diagonal2/2
    return area

print("el area del rombo es",area_rombo(30,16))
    
def area_circulo(radio):
    area= math.pi*radio**2
    return area

print("el area del circulo es",area_circulo(6))