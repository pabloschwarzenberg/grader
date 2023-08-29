from math import pi

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
    area = pi*radio**2
    return area


if __name__ == '__main__':
    sw = True
    while sw:
        print('Calculadora de areas')
        print()
        print('1.- Triangulo')
        print('2.- Rectangulo')
        print('3.- Rombo')
        print('4.- Circulo')
        print('0.- Salir')
        print()
        x = input('Que calculo desea realizar?: ')
        if x == '0':
            sw = False
        elif x=='1':
            base = float(input('Ingrese valor de la base: '))
            altura = float(input('Ingrese valor de la altura: '))
            print('Area:',area_triangulo(base,altura))
        elif x=='2':
            base = float(input('Ingrese valor de la base: '))
            altura = float(input('Ingrese valor de la altura: '))
            print('Area:',area_rectangulo(base,altura))
        elif x=='3':
            d1 = float(input('Ingrese valor de la diagonal1: '))
            d2 = float(input('Ingrese valor de la diagonal2: '))
            print('Area:',area_rombo(d1,d2))
        elif x=='4':
            r = float(input('Ingrese valor del radio: '))
            print('Area:',area_circulo(r))
        else:
            print('Error, no se reconoce la opcion ingresada')
           