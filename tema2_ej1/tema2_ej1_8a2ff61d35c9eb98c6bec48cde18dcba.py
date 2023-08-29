from math import pi,sen
def area_triangulo(base,altura):
    r=(base*altura)/2
    return r

def area_rectangulo(base,altura):
     r=base*altura
     return r

def area_rombo(diagonal1,diagonal2):
     r=(diagonal1*diagonal2)*sen
     
def area_circulo(radio):
     r=(radio**2)*pi
     return r
if __name__ == "__main__":
    pass
           