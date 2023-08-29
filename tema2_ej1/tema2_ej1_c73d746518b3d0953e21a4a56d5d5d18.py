import math 
def area_triangulo(base,altura):
    atriangulo = (base*altura)/2
    return atriangulo

def area_rectangulo(base,altura):
    arectangulo = (base*altura)
    return arectangulo

def area_rombo(diagonal1,diagonal2):
    arombo= (diagonal1*diagonal2)/2
    return arombo

def area_circulo(radio):
    
    acirculo = float(pow(radio,2)*math.pi)
    return acirculo
           