import math
def area_triangulo(base,altura):
    a=(base*altura)/2
    b=round(a,1)
    return b
def area_rectangulo(base,altura):
    a=base*altura
    b=round(a,1)
    return b

def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    b=round(a,1)
    return b 

def area_circulo(radio):
    b=(radio**2)*math.pi
    
    return b 
 

           