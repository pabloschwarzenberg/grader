from math import*
def area_triangulo(base,altura):
    base=float(base)
    altura=float(altura)
    area=(base*altura)/2
    return area
    pass

def area_rectangulo(base,altura):
    base=float(base)
    altura=float(altura)
    area=base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    diag1=float(diagonal1)
    diag2=float(diagonal2)
    area=diag1*diag2/2
    return area
    pass

def area_circulo(radio):
    rad=float(radio)
    area=pi*(rad**2)
    return area
    pass

if __name__ == "__main__":
    pass
           