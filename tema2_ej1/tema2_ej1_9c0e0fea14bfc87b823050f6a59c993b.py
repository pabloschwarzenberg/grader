import math
math.pi #codigo para obtener el numero pi = (math.pi)
print("1. Area del Triagulo")
print("2. Area del Rectangulo")
print("3. Area del Rombo")
print("4. Area del Circulo")


# Calculo del Triangulo 


def area_triangulo(base,altura):
    calculo = (base * altura) /2
    return calculo 
    pass


# Calculo del Rectangulo 


def area_rectangulo(base,altura):
    calculo = base * altura
    return calculo 
    pass


# Calculo del Rombo

def area_rombo(diagonal1,diagonal2):
    calculo = (diagonal1 * diagonal2) / 2
    return calculo 
    pass


# Calculo del Circulo 


def area_circulo(radio):
    calculo = radio*radio*math.pi
    return calculo 
    pass
