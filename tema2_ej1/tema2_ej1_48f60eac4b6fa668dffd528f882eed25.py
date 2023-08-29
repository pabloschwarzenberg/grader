from math import pi

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
def area_rectangulo(base, altura):
    area = base * altura 
    return area
def area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area
def area_circulo(radio):
    area = (2 * pi * radio ** 2 )/ 2
    return area
if __name__ == "__main__":
    figuras = str(input(" ingrese la figura que desea realizar(circulo, rombo, rectangulo, triangulo): "))
    if (True):
        figuras.lower()
    if (figuras == "circulo"):
        area = area_circulo(input(" ingrese el radio: "))
    if (figuras == "rombo"):
        area = area_rombo(input(" ingrese la diagonal 1: "), input(" ingrese la diagonal 2: "))
    if (figuras == "rectangulo"):
        area = area_rectangulo(input(" ingrese la base: "), input(" ingrese la altura: "))
    if (figuras == "triangulo"):
        area = area_triangulo(input(" ingrese la base: "), input(" ingrese la altura: "))
  
           