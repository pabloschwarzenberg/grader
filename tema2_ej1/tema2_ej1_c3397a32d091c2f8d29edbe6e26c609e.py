def area_triangulo(base,altura):
    areaTring=(base*altura)/2
    return areaTring

def area_rectangulo(base,altura):
    areaRec=base*altura
    return areaRec

def area_rombo(diagonal1,diagonal2):
    areaRom=diagonal1*diagonal2/2
    return areaRom

def area_circulo(radio):
    from math import pi
    areaCirc=(radio**2)*pi
    return areaCirc

if __name__ == "__main__":
    pass
           