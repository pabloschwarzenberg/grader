from math import pi
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=(base*altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=radio**2*pi
    return area

print("1.Área de un triángulo")
print("2.Área de un rectángulo")
print("3.Área de un rombo")
print("3.Área de un circulo")
