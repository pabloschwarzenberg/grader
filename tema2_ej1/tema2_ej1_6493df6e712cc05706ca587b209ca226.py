import math
def area_triangulo(base,altura):
    area_tri = (base * altura)/2
    return area_tri
                                            
def area_rectangulo(base,altura):
    area_rec = (base*altura)
    return area_rec

def area_rombo(diagonal,diagonal_2):
    area_rom = (diagonal*diagonal_2)/2
    return area_rom
    
def area_circulo(radio):
    pi = math.pi
    area_cir = pi * (radio**2)
    return area_cir

           