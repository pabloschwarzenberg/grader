import math
def area_triangulo(base,altura):
    area=(int(base)*int(altura))/2
    return area

def area_rectangulo(base,altura):
    area=int(base)*int(altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area=(int(diagonal1)*int(diagonal2))/2
    return area

def area_circulo(radio):
    area=math.pi*(int(radio)**2)
    return area

if __name__ == "__main__":
    pass
           