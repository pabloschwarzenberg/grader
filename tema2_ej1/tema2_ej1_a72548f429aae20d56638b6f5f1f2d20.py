import math

def area_triangulo(base, altura):
    areaUno = base * altura / 2
    return print("El área del triángulo es: ", areaUno)

def area_rectangulo(base, altura):
    areaDos = base * altura
    return print("El área del rectangulo es: ", areaDos)

def area_rombo(diagonal1, diagonal2, alturaUno):
    areaTres = (diagonal1 + diagonal2) * alturaUno / 2
    return print("El área del trapecio es: ", areaTres)

def area_circulo(radio):
    areaCuatro = math.pi * radio ** 2
    return print("El área del circulo es: ", areaCuatro)
           