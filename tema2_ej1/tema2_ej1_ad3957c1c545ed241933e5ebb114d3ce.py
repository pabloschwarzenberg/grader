import math

def area_triangulo(base, altura):
    #base = int(input("base triangulo: "))
    #altura = int(input("altura triangulo: "))
    area = (base*altura)/2
    return area
    pass

def area_rectangulo(base, altura):
    #base = int(input("base rectangulo: "))
    #altura = int(input("altura rectangulo: "))
    area = base*altura
    return area
    pass

def area_rombo(diagonal1 ,diagonal2):
    #diagonal1 = int(input("diagonal1 rombo: "))
    #diagonal2 = int(input("diagonal2 rombo: "))
    area = (diagonal1*diagonal2)/2
    return area
    pass

def area_circulo(radio):
    #radio = int(input("radio circulo: "))
    area = 3.141592653589793*(radio**2)
    return area
    pass

#area_triangulo()
#area_rectangulo()
#area_rombo()
#area_circulo()