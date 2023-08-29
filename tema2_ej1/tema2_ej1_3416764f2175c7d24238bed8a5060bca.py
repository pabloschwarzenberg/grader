from math import pi

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
    area = pi*radio**2
    return area

def menu():
    print('              menu')
    print('     1) area triangulo')
    print('     2) area rectangulo')
    print('     3) area rombo')
    print('     4) area circulo')

    x = int(input('ingrese una opcion:'))

    if x==1:
        b=int(input('ingresa base:'))
        a=int(input('ingresa altura:'))
        
        area = area_triangulo(b,a)
        return area

    if x==2:
        b=int(input('ingresa base:'))
        a=int(input('ingresa altura:'))
        
        area = area_rectangulo(b,a)
        return area

    if x==3:
        b=int(input('ingresa diagonal 1:'))
        a=int(input('ingresa diagonal 2:'))
        
        area = area_rombo(b,a)
        return area

    if x==4:
        r = int(input('ingresa radio:'))
        area = area_circulo(r)

        return area

           