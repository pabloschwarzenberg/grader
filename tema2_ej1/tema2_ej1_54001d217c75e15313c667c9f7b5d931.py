"""
def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
"""

def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

def area_triangulo(base, altura):
    resultado = (base * altura)/2
    return resultado

def area_rombo(diagonal1, diagonal2):
    resultado = (diagonal1 * diagonal2)/2
    return resultado

def area_circulo(radio):
    from math import pi
    resultado = pi * (radio**2)
    return resultado
           