from math import pi

def area_triangulo(base,altura):
    return base * altura/2

def area_rectangulo(base,altura):
    return base * altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 / 2

def area_circulo(radio):
    return pi * radio ** 2

if __name__ == "__main__":
    op = input('¿Qué área deseas calcular? ').lower().strip()

    if op == 'triangulo':
      base = float(input('Ingrese base: '))
      altura = float(input('Ingrese altura: '))
      print(area_triangulo(base,altura))

    elif op == 'rectangulo':
      base = float(input('Ingrese base: '))
      altura = float(input('Ingrese altura: '))
      print(area_rectangulo(base,altura))

    elif op == 'rombo':
      d1 = float(input('Ingrese diagonal1: '))
      d2 = float(input('Ingrese diagonal2: '))
      print(area_rombo(d1,d2))

    elif op == 'circulo':
      r = float(input('Ingrese radio: '))
      print(area_circulo(r))

