import math
# Declaración de las funciones
def area_triangulo(base,altura):
    art = (base*altura)/2
    return art

def area_rectangulo(base,altura):
    arc = base*altura
    return arc
    
def area_rombo(diagonal1,diagonal2):
    arm = (diagonal1*diagonal2)/2
    return arm
   
def area_circulo(radio):
    acir = math.pi * radio**2
    return acir