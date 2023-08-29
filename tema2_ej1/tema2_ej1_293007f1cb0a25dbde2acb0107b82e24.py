import math
def area_triangulo(base,altura):
    area1 = (base * altura) / 2
    return area1

def area_rectangulo(base,altura):
    area2 = base * altura
    return area2

def area_rombo(diagonal1,diagonal2):
    area3 = (diagonal1 * diagonal2) / 2
    return area3

def area_circulo(radio):
    pi = math.pi
    area4 = pi * radio ** 2
    return area4
def numero_perfecto(a):
    contador = 1
    suma = 2
    while contador < a :
        if a % contador == 0 :
            suma = suma + contador
            print(suma, contador)
            contador += 1
        contador += 1
    if suma == a :
        return True
    else:
        return False
           