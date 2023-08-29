import math

def area_triangulo(base,altura):
    area=float((base*altura)/2)
    return area



def area_rectangulo(base,altura):
    area=float(base*altura)
    return area




def area_rombo(diagonal1,diagonal2):
    area=float((diagonal1*diagonal2)/2)
    return area



def area_circulo(radio):
    area=float((math.pi*(radio**2)))
    return area



if __name__ == "__main__":
    print(area_triangulo(2,3))
    print(area_rectangulo(2,3))
    print(area_rombo(2,3))
    print(area_circulo(40))