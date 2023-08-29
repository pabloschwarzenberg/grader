import math

def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area =  (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    area = math.pi * radio **2
    return area

if __name__ == "__main__":

    while True:

        print('(1) Triángulo \n'
              '(2) Rectángulo \n'
              '(3) Rombo \n'
              '(4) Círculo\n'
              '(5) Salir \n'
              '')
        figura = int(input('Elija la figura de la cual quiera calcular el area: '))

        if figura == 1:
            h = float(input('Ingrese la altura: '))
            b = float(input('Ingrese el largo de la base: '))
            area = area_triangulo(b,h)
        elif figura ==  2:
            h = float(input('Ingrese la altura: '))
            b = float(input('Ingrese el largo de la base: '))
            area = area_rectangulo(b,h)
        elif figura == 3:
            d1 = float(input('Ingrese el largo de la primera diagonal: '))
            d2 = float(input('Ingrese el largo de la segunda diagonal: '))
            area = area_rombo(d1,d2)
        elif figura == 4:
            r = float(input('Ingrese el radio: '))
            area = area_circulo(r)
        elif figura == 5:
            break

        print(area)