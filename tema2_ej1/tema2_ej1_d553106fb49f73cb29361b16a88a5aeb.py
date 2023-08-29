import math
def area_triangulo(base,altura):
    area = base * altura / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

if __name__ == "__main__":
    while True:
        opcionMenu = input("selecione una opcion:(1)triangulo(2)rectangulo(3)rombo(4)circulo(5)salir: ")
        if opcionMenu == 1:
          base = int(input("ingrese base: "))
          altura = int(input("ingrese altura: "))
          area.area_triangulo(base,altura)
        if opcionMenu == 2:
          base = int(input("ingrese base: "))
          altura = int(input("ingrese altura: "))
          area.area_rectangulo(base,altura)
        if opcionMenu ==3:
          diagonal1 = int(input("ingrese diagonal1: "))
          diagonal2 = int(input("ingrese diagonal2: "))
          area.area_rombo(diagonal1,diagonal2)
        if opcionMenu == 4:
          radio = int(input("ingrese radio: "))
          area.area_circulo
        if opcionMenu == 5:
            break
