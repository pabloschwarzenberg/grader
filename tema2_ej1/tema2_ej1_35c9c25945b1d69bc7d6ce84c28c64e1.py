#Calculadora Geometrica
def area_triangulo(base,altura):
    Triangulo = (base*altura)/2
    return Triangulo
   
def area_rectangulo(base,altura):
    Rectangulo = base*altura
    return Rectangulo

def area_rombo(diagonal1,diagonal2):
    Rombo = (diagonal1*diagonal2)/2
    return Rombo

def area_circulo(radio):
    pi = 3.1415926535897932
    Circulo = pi*radio**2
    return Circulo
