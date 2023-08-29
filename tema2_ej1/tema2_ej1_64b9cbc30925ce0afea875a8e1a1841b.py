import math
def area_triangulo(base,altura):
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    radio = float(radio)
    area = float(radio*radio*math.pi)
    return area

if __name__ == "__main__":
    a = input("poligono a calcular")
    if a == "triangulo":
        print(area_triangulo(base=input("altura"),altura=input("altura")))

    elif a == "rectangulo":
        print(area_rectangulo(base=input("base"),altura=input("base")))
    elif a == "circulo":
        print(area_circulo(radio=input("radio")))
    else:
        print(area_rombo(diagonal1=input("d_1"),diagonal2=input("d_2")))
    
           