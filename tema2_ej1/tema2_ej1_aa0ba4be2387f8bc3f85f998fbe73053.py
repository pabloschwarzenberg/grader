import math

def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=(radio**2)*math.pi
    return area

print("escoja la figura geometrica a calcular")
print("\n1.Triangulo\n2.rectangulo\n3.rombo\n4.circulo\n5.salir")
      