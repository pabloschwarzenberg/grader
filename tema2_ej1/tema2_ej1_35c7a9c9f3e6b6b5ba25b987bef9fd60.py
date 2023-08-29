import math

def area_triangulo(base,altura):
    atg_r=((base*altura)/2)
    return atg_r

def area_rectangulo(largo,ancho):
    art_r=(largo*ancho)
    return art_r

def area_rombo(diagonal1,diagonal2):
    arb_r=((diagonal1*diagonal2)/2)
    return arb_r

def area_circulo(radio):
    acl_r=(math.pi*(radio**2))
    return acl_r