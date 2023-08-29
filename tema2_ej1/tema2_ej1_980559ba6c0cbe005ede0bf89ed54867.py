from math import pi

def area_triangulo(base,altura):
    area = base * altura
    area = area / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2
    area = area / 2
    return area

def area_circulo(radio):
    area = pi*(radio**2)
    return area

'''print('1. Area Triangulo')
print('2. Area Rectangulo')
print('3. Area Rombe')
print('4. Area Circulo')


a =int(input("Ingrese un numero de figura para calcular area: "))

if a == 1:
    base = int(input('Ingrese base'))
    altura = int(input('Ingrese altura'))
    area_triangulo(base,altura)
elif a == 2:
    base = int(input('Ingrese base'))
    altura = int(input('Ingrese altura'))
    area_rectangulo(base,altura)
elif a == 3:
    diagonal1 = int(input('Ingrese primera diagonal'))
    diagonal2 = int(input('Ingrese segunda diagonal'))
    area_rombo(diagonal1,diagonal2)
elif a == 4:
    radio = int(input('Ingrese radio'))
    area_circulo(radio)
else:
    pass'''