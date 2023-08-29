import math

def area_triangulo(base,altura):

    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):

    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):

    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):

    area = radio*radio*math.pi
    return area

if __name__ == "__main__":

    opcion = 1

    while opcion != 0:

        print('Elija una Opcion')
        print('1: Area Triangulo')
        print('2: Area Rectangulo')
        print('3: Area Rombo')
        print('4: Area Circulo')
        print('0: Salir')

        opcion = int(input('Opcion: '))

        if opcion == 1:
            base = float(input('Base: '))
            altura = float(input('Altura: '))
            print('El area es: '+str(area_triangulo(base,altura)))
        elif opcion == 2:
            base = float(input('Base: '))
            altura = float(input('Altura: '))
            print('El area es: '+str(area_rectangulo(base,altura)))
        elif opcion == 3:
            diagonal1 = float(input('Diagonal 1: '))
            diagonal2 = float(input('Diagonal 2: '))
            print('El area es: '+str(area_rombo(diagonal1,diagonal2)))
        elif opcion == 4:
            radio = float(input('Radio: '))
            print('El area es: '+str(area_circulo(radio)))
        elif opcion == 0:
            print('Saliendo ....')
        else:
            print('Error en opcion ...')

           