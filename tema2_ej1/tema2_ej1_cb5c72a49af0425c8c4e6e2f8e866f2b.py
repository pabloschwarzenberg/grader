#calculadora

import math

def area_triangulo(base, altura):
    return base * altura / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return diagonal1 * diagonal2 / 2

def area_circulo(radio):
    return math.pi * radio * radio

if __name__ == "__main__":
    print("Que desea calcular?")
    print("1. Area de un triangulo")
    print("2. Area de un rectangulo")
    print("3. Area de un rombo")
    print("4. Area de un circulo")
    opcion = int(input())

    if opcion == 1:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Area: " + str(area_triangulo(base, altura)))
    elif opcion == 2:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Area: " + str(area_rectangulo(base, altura)))
    elif opcion == 3:
        diagonal1 = float(input("Diagonal 1: "))
        diagonal2 = float(input("Diagonal 2: "))
        print("Area: " + str(area_rombo(diagonal1, diagonal2)))
    elif opcion == 4:
        radio = float(input("Radio: "))
        print("Area: " + str(area_circulo(radio)))
    else:
        print("Opcion invalida! Intente nuevamente")