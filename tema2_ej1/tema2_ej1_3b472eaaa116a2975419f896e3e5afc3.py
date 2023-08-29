from math import pi 
def area_triangulo(base,altura):
    area=base*altura/2
    return area 
    pass

def area_rectangulo(base,altura):
    area=base*altura
    return area 
    pass

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area 
    pass

def area_circulo(radio):
    area=(radio**2)*pi
    return area 
    pass

if __name__ == "__main__":
    print(area_circulo(2))
    print(area_rectangulo(2,3))
    print(area_triangulo(2,2))
    print(area_rombo(2,4))
    pass

           