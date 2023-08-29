from cmath import pi


def area_triangulo(base,altura):

    area_tr = (base*altura)/2

    return area_tr

def area_rectangulo(base,altura):
    
    area_rec = base*altura

    return area_rec

def area_rombo(diagonal1,diagonal2):
    
    area_rom = (diagonal1*diagonal2)/2
    return area_rom

def area_circulo(radio):
    
    area_cir = pi*(radio)**2
    return area_cir