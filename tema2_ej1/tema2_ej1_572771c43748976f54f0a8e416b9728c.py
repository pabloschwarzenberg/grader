import math
def area_triangulo(base,altura):
    sal_a_t=(base*altura)/2
    return (sal_a_t)

def area_rectangulo(base,altura):
    sal_a_r= base*altura
    return(sal_a_r)

def area_rombo(diagonal1,diagonal2):
    sal_a_rom=(diagonal1*diagonal2)/2
    return(sal_a_rom)

def area_circulo(radio):
    sal_a_c=(math.pi)*(radio**2)
    return(sal_a_c)