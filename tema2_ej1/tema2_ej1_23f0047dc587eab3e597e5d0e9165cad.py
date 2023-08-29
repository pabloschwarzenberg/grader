import math

def area_triangulo(base,altura):
    area=(base*altura)/2
    
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    x=(diagonal1/2)
    y=(diagonal2/2)
    
    area=((x*y)/2)*4
    return area

def area_circulo(radio):
    pi=math.pi
    area=pi*radio**2
    
    return area

if __name__ == "__main__":
    pass
           