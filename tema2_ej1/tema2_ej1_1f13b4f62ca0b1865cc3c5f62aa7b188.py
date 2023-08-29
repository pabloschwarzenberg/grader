from math import pi


def area_triangulo(base, altura):
    area = base * altura * 0.5
    return area


def area_rectangulo(base, altura):
    area = base * altura
    return area


def area_rombo(diagonal1, diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area


def area_circulo(radio):
    area = pi * radio ** 2
    return area


if __name__ == "__main__":
    while True:
        print("Seleccione el calculo que desea efectuar: ")
        print(" 1 - Area Triangulo")
        print(" 2 - Area Rectanngulo")
        print(" 3 - Area Rombo")
        print(" 4 - Area Circulo")
        print("\nPara seleccionar, ingrese el numero correspondiente: ")
        opt = input('-> ')
        if int(opt) in [1, 2, 3, 4]:
            break
        else:
            print('\n La opcion ingresada no es valida.\n\nPor favor, ')

    if opt == '1':
        print()
        print('Ingrese los parametros del Trianngulo: ')

        b = float(input('Base: '))
        a = float(input('Altura: '))

        print('\nEl Area del Triangulo ingresado es: ')
        print(area_triangulo(b, a))

    elif opt == '2':
        print()
        print('Ingrese los parametros del Rectanngulo: ')

        b = float(input('Base: '))
        a = float(input('Altura: '))

        print('\nEl Area del Rectangulo ingresado es: ')
        print(area_rectangulo(b, a))

    elif opt == '3':
        print()
        print('Ingrese los parametros del Rombo: ')

        d_1 = float(input('Diagonal 1: '))
        d_2 = float(input('Diagonal 2: '))

        print('\nEl Area del Rombo ingresado es: ')
        print(area_rombo(d_1, d_2))

    elif opt == '4':
        print()
        print('Ingrese el radio del Ciculo: ')

        r = float(input('Radio: '))

        print('\nEl Area del Circulo ingresado es: ')
        print(area_circulo(r))
