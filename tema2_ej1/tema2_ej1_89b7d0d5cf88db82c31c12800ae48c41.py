area = 1
area_triangulo = 1
area_rectangulo = 1
area_rombo = 1 
area_circulo = 1



from math import pi

def area_triangulo(base, altura):

    area = (base * altura) / 2

    return area

def area_rectangulo(base, altura):

    area = base * altura

    return area

def area_rombo(diagonal_1, diagonal_2):

    area = (diagonal_1 * diagonal_2) / 2

    return area

def area_circulo(radio):

    area = (2 * pi * radio ** 2 )/ 2

    return area