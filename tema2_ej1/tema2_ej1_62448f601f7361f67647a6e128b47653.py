import math

def area_triangulo(base, altura):
    area_t = (base * altura) / 2
    return area_t

def area_rectangulo(base, altura):
    area_r = base * altura
    return area_r

def area_rombo(diagonal1, diagonal2):
    area_ro = (diagonal1 * diagonal2) / 2 
    return area_ro

def area_circulo(radio):
    area_c =  math.pi * (radio * radio)
    return area_c

if __name__ == "__main__":
    print("Bienvenido, qué área desea calcular?")
    print("1. Área de un triángulo")
    print("2. Área de un rectángulo")
    print("3. Área de un rombo")
    print("4. Área de un circulo")
    nro = int(input("Ingrese su elección: "))

    if nro == 1:
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese su altura: "))
        area = area_triangulo(a, b)
        print("El área es:", area)
    elif nro == 2:
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese su altura: "))
        area = area_rectangulo(a, b)
        print("El área es:", area)
    elif nro == 3:
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese su altura: ")) 
        area = area_rombo(a, b)
        print("El área es:", area)
    elif nro == 4:
        radio = int(input("Ingrese el radio: "))
        area = area_circulo 
        print("El área es:", area)
    else:
        print("Selección inválida")

           