import math

def area_triangulo(base,altura):
    area_triangulo = (base*altura) / 2
    return area_triangulo
    pass

def area_rectangulo(base,altura):
    area_rectangulo = base*altura
    return area_rectangulo
    pass

def area_rombo(diagonal1,diagonal2):
    area_rombo= (diagonal1*diagonal2) / 2
    return area_rombo
    pass

def area_circulo(radio):
    area_circulo = math.pi * radio **2
    return area_circulo
    pass

def menu_calculadora():
    for opcion in menu_calculadora():
        
        if opcion == "1":
            resultado = area_triangulo(base,altura)
        elif opcion == "2":
            resultado = area_rectangulo(base,altura)
        elif opcion == "3":
            resultado = area_rombo(diagonal1,diagonal2)
        elif opcion == "4":
            resultado = area_circulo(radio)
        return resultado