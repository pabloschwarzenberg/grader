import math
def area_triangulo(base,altura):
    areaT=(base*altura)/2
    return areaT
def area_rectangulo(base,altura):
    areaRec = base*altura
    return areaRec

def area_rombo(diagonal1,diagonal2):
    areaRom = (diagonal1*diagonal2) / 2
    return areaRom

def area_circulo(radio):
    areaC= (radio**2)*math.pi
    return areaC           