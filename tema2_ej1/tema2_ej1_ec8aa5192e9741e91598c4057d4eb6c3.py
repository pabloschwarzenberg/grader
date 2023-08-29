from math import pi

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return base * altura / 2

def area_circulo(radio):
    return pi * radio ** 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return diagonal_mayor * diagonal_menor / 2

if __name__ == "__main__":
    opcion = input('¿Qué deseas calcular? (R)ectángulo, (T)riángulo, (C)írculo, (R)ombo: ')
    if opcion.upper() == 'R':
        base = float(input('Dame la base: '))
        altura = float(input('Dame la altura: '))
        print('El área del rectángulo es:', area_rectangulo(base, altura))
    elif opcion.upper() == 'T':
        base = float(input('Dame la base: '))
        altura = float(input('Dame la altura: '))
        print('El área del triángulo es:', area_triangulo(base, altura))
    elif opcion.upper() == 'C':
        radio = float(input('Dame el radio: '))
        print('El área del círculo es:', area_circulo(radio))
    elif opcion.upper() == 'R':
        diagonal_mayor = float(input('Dame la diagonal mayor: '))
        diagonal_menor = float(input('Dame la diagonal menor: '))
        print('El área del rombo es:', area_rombo(diagonal_mayor, diagonal_menor))
    else:
        print('Opción inválida. Por favor, selecciona una opción válida.')
