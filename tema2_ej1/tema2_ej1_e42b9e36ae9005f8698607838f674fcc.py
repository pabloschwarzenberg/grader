import math


def area_triangulo(base, altura):
    return 0.5 * base * altura


def area_rectangulo(base, altura):
    return base * altura


def area_rombo(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2


def area_circulo(radio):
    return math.pi * radio**2


if __name__ == "__main__":
    print('¿De qué figura quieres calcular el área?')
    print('# 1: Triángulo')
    print('# 2: Rectángulo')
    print('# 3: Rombo')
    print('# 4: Círculo')
    command = input('Escribe el número 1, 2, 3 o 4 para seleccionar.\n')
    if command == "1":
        TempA = int(input('Ingresa la base: '))
        TempB = int(input('Ingresa la altura: '))
        print('El área es ' + str(area_triangulo(TempA, TempB)))
    elif command == "2":
        TempA = int(input('Ingresa la base: '))
        TempB = int(input('Ingresa la altura: '))
        print('El área es ' + str(area_rectangulo(TempA, TempB)))
    elif command == "3":
        TempA = int(input('Ingresa una diagonal: '))
        TempB = int(input('Ingresa la otra: '))
        print('El área es ' + str(area_rombo(TempA, TempB)))
    else:
        TempA = int(input('Ingresa el radio: '))
        print('El área es ' + str(area_circulo(TempA)))
