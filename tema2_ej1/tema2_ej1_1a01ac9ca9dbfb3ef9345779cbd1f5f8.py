import math
def area_triangulo(base,altura):
    areat = base*altura/2
    return(areat)
def area_rectangulo(base,altura):
    area_rect= base*altura
    return(area_rect)

def area_rombo(diagonal1,diagonal2):
    area_romb= diagonal1*diagonal2/2
    return(area_romb)

def area_circulo(radio):
    area_circ=math.pi*radio**2
    return(area_circ)

if __name__ == "__main__":
    pass
           