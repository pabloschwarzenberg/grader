import math

def menu():
    print("Calcular Áreas de figuras Geométricas.\n")
    print("1.Cuadrado.\n2.Circulo.\n3.Triángulo.\n4.Trapecio.\n")
    n = int(input("Numero: "))
    return ""

if n == 3:
    b = int(input('Ingrese la base: '))
    h = int(input('Ingrese la altura: '))
def area_triangulo(base, altura):
    area = base * altura/2
    return print("El area del triangulo es: ", area)


#if area_triangulo(base,altura):
    #area = base * altura/2
   # return print("El area del triangulo es: ", area)


def area_rectangulo(base,altura):
    area = base * altura
    return print("El area del rectangulo es: ",area)

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return print("El area del rombo es: ", area)

def area_circulo(radio):
    area = math.pi*radio**2
    return print("El area del circulo es: %.3f "% area)

menu()
