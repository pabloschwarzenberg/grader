import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    print('el area del triangulo es: ', area)
    return area

def area_rectangulo(base,altura):
    area=base*altura
    print('el area del rectangulo es: ', area)
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    print('el area del rombo es: ',area)
    return area

def area_circulo(radio):
    area=math.pi*radio**2
    print('el area del circulo es: ',area)
    return area

if __name__ == "__main__":
    a=input('el area de que figura quieres calcular?: ')
    if a=='triangulo':
        b=input('base: ')
        h=input('altura: ')
        area_triangulo(b,h)
    elif a==rectangulo:
        b=input('base: ')
        h=input('altura: ')
        area_rectangulo(b,h)
    elif a==rombo:
        b=input('diagonal 1: ')
        h=input('diagonal 2: ')
        area_rombo(b,h)
    elif a==circulo:
        b=input('radio: ')
        area_circulo(b)