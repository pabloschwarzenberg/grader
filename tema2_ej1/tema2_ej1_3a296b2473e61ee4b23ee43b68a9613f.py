def area_triangulo(base,altura):
    area= (base*altura)/2
    return area
    
def area_rectangulo(base,altura):
    area= base*altura
    return area
    
def area_rombo(diagonala,diagonalb):
    area= (diagonala*diagonalb)/2
    return area
    
def area_circulo(r):
    import math
    area= math.pi * (r**2)
    return area         