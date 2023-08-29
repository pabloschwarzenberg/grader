
import math

def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    area = (radio ** 2) * math.pi
    return area

if __name__ == "__main__":
    print('Seleciones lo que desea calcular' )
    print('1.- Triángulo '
          '\n2.- Rectángulo'
          '\n3.- Rombo'
          '\n4.- Cíirculo')
    opcion= int(input('ingrese su opción: '))
    if opcion == 1:
        dato1 = int(input('Ingrese la base  : '))
        dato2 = int(input('Ingrese la altura: '))
        print(area_triangulo(dato1, dato2))
    if opcion == 2:
        dato1 = int(input('Ingrese la base  : '))
        dato2 = int(input('Ingrese la altura: '))
        print(area_rectangulo(dato1, dato2))
    if opcion == 3:
        dato1 = int(input('Ingrese diagonal1  : '))
        dato2 = int(input('Ingrese diagonal2: '))
        print(area_rombo(dato1, dato2))
    if opcion == 4:
        dato1 = int(input('Ingrese diametro  : '))
        print(area_circulo(dato1))
           