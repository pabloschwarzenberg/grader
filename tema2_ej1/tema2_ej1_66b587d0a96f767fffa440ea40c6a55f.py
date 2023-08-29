import math

def area_triangulo(base,altura):
    Atri = (base * altura)/2
    return Atri
    pass

def area_rectangulo(base,altura):
    Arec = base * altura
    return Arec
    pass

def area_rombo(diagonal1,diagonal2):
    Arom = (diagonal1 * diagonal2)/2
    return Arom
    pass

def area_circulo(radio):
    Acir = math.pi * radio**2
    return Acir
    pass

if __name__ == "__main__":
    pass
           