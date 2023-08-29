from math import pi 
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area    
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area=pi*radio**2
    return area
def proOpciones(opcion):
    if opcion==1:
        base=int(input('ingresa la base del triangulo: '))
        altura=int(input('ingresa la altura del triangulo: '))
        area=area_triangulo(base, altura)
        print('el area del triangulo es: ',area)
    if opcion==2:
        base=int(input('ingresa la base del rectangulo: '))
        altura=int(input('Ingresa la altura del rectangulo: '))
        area=area_rectangulo(base,altura)
        print('el area del Rectangulo es: ', area)        
    if opcion==3:
        diagonal1=int(input('ingrese la diagonal 1 del rombo: '))
        diagonal2=int(input('ingrese la diagonal 2 del rombo: '))
        area=area_rombo(diagonal1, diagonal2)
                   
    if opcion==4:
        radio=int(input('Ingresa el area del circulo: '))
        area=area_circulo(radio)
        print('el area del circulo es: ', area)

def menu():
    opcion=1
    while opcion!=5:
        
        print('\n    Menu')
        print('1. Area Triangulo')
        print('2. Area Rectangulo')
        print('3. Area Rombo')
        print('4. Area Circulo')
        print('5. Salir')
        opcion=int(input('Ingresa una opcion: '))
        proOpciones(opcion)
    print('Sesion Finalizada')  