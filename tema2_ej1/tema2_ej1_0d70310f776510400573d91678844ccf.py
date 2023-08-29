import math
def area_triangulo(base,altura):
    b = base
    a = altura
    n=b*a/2
    return n

def area_rectangulo(base,altura):
    a = altura
    b = base
    n=b*a
    return n

def area_rombo(diagonal1,diagonal2):
    n=diagonal1*diagonal2//2
    return n

def area_circulo(radio):
    
    n= math.pi*radio**2
    return n

if __name__ == "__main__":
    pass
           