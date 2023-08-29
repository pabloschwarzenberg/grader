import math
def area_triangulo(base,altura):
    area1=int(base)*int(altura)/2
    return area1

def area_rectangulo(base,altura):
    area2=int(base)*int(altura)
    return area2

def area_rombo(diagonal1,diagonal2):
    area3=int(diagonal1)*int(diagonal2)/2
    return area3

def area_circulo(radio):
    area=math.pi*(int(radio))**2
    return area

           