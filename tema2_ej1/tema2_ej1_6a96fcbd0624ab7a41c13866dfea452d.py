from math import pi
def area_triangulo(base,altura):
    return base * altura / 2

def area_rectangulo(base,altura):
    return base * altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 / 2

def area_circulo(radio):
    return pi * radio ** 2

if __name__ == "__main__":
    seleccion = input()
    base = input()
    altura = input()
    
    opciones = {
    "triangulo":area_triangulo(base, altura),
    "rectangulo":area_triangulo(base, altura),
    "rombo":area_triangulo(base, altura),
    "circulo":area_triangulo(base, altura)}
    
    opciones[seleccion]
    
           