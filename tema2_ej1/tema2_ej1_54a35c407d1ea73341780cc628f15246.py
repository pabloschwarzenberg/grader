import math

def area_triangulo(base,altura):
    calculo=(base*altura)/2
    return calculo

def area_rectangulo(base,altura):
    calculo=base*altura
    return calculo

def area_rombo(diagonal1,diagonal2):
    calculo=(diagonal1*diagonal2)/2
    return calculo

def area_circulo(radio):
    pi=math.pi
    calculo=pi*(radio**2)
    return calculo

print('MENU:')
print('\n')
print('1. area triangulo')
print('2. area rectangulo')
print('3. area rombo')
print('4. area circulo')
print('\n')
base=0
altura=0
radio=0
diagonal1=0
diagonal2=0
opcion=4
while opcion>4 or opcion<1:
    print('MENU:')
    print('\n')
    print('1. area triangulo')
    print('2. area rectangulo')
    print('3. area rombo')
    print('4. area circulo')
    print('\n')
    opcion=int(input('opcion: '))
if opcion==1:
    base=1
    altura=2
    area_triangulo(base,altura)
    print(area_triangulo(base,altura))
if opcion==2:
    base=1
    altura=2
    area_rectangulo(base,altura)
    print(area_rectangulo(base,altura))
if opcion==3:
    diagonal1=1
    diagonal2=2
    area_rombo(diagonal1,diagonal2)
    print(area_rombo(diagonal1,diagonal2))
if opcion==4:
    radio=40
    area_circulo(radio)
    print(area_circulo(radio))