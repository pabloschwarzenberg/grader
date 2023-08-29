from math import pi

def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    return pi * (radio ** 2)

if __name__ == '__main__':
    case = int(input("""¿Qué área desea calcular? Ingresa el número:
1 para área de triángulo.
2 para área de rectángulo
3 para área de rombo.
4 para área de círculo
Ingresa 0 para salir: """))
    
    if case == 1:
        base = int(input('Ingrese la base: '))
        altura = int(input('Ingrese la altura: '))
        #print(f'El área del triángulo es {area_triangulo(base,altura)}')
        print(area_triangulo(base,altura))
    elif case == 2:
        base = int(input('Ingrese la base: '))
        altura = int(input('Ingrese la altura: '))
        #print(f'El área del rectángulo es {area_rectangulo(base,altura)}')
        print(area_rectangulo(base,altura))
    elif case == 3:
        diagonal1 = int(input('Ingrese la medida de la diagonal 1: '))
        diagonal2 = int(input('Ingrese la medida de la diagonal 2: '))
        #print(f'El área del rombo es {area_rombo(diagonal1, diagonal2)}')
        print(area_rombo(diagonal1, diagonal2))
    elif case == 4:
        radio = int(input('Ingrese la medida del radio: '))
        #print(f'El área del círculo es {area_circulo(radio)}')
        print(area_circulo(radio))
    elif case == 0:
        print('Hasta pronto.')
           