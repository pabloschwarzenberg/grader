import math
def area_triangulo(base,altura):
        base = float(base)
        altura = float(altura)
        area_triangulo = (base * altura)/2
        return area_triangulo

def area_rectangulo(base,altura):
        base = float(base)
        altura = float(altura)
        area_rectangulo = base * altura
        return area_rectangulo

def area_circulo(radio):
        radio = float(radio)
        area_circulo = math.pi * radio ** 2
        return area_circulo

def area_rombo(diagonal1,diagonal2):
        diagonal1 = float(diagonal1)
        diagonal2 = float(diagonal2)
        area_rombo = (diagonal1 * diagonal2)/2
        return area_rombo


    
    
           