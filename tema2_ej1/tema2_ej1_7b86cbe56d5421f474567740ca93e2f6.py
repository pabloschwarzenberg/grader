import math

def area_triangulo(base, altura):
    triangulo = base*altura/2
    return triangulo
    pass 

def area_rectangulo(base, altura):
    rectangulo = base*altura
    return rectangulo
    pass

def area_rombo(diagonal1, diagonal2):
    rombo = diagonal1*diagonal2/2
    return rombo
    pass

def area_circulo(radio):
    circulo = math.pi*(radio**2)
    return circulo
    pass

if __name__ == "__main__":
    ask = input('¿Qué área desea sacar?: ')
    if ask == "triangulo":
        base = int(input('Ingrese base: '))
        altura = int(input('Ingrese altura: '))
        print(area_triangulo(base, altura))
    elif ask == "rectangulo":
        base = int(input('Ingrese base: '))
        altura = int(input('Ingrese altura: '))
        print(area_rectangulo(base, altura))
    elif ask == "rombo":
        diagonal1 = int(input('Ingrese diagonal 1:'))
        diagonal2 = int(input('Ingrese diagonal 2:'))
        print(area_rombo(diagonal1, diagonal2))
    elif ask == "circulo":
        radio = int(input('Ingrese radio: '))
        print(area_circulo(radio))