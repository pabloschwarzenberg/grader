def suma_divisores(n):
    suma = 0
    for i in range(1,n):
        if n%i == 0:
            suma += i
    if suma == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    print(suma_divisores(n))

import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(area_rectangulo(base, altura))
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(area_triangulo(base, altura))
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        print(area_rombo(diagonal_mayor, diagonal_menor))
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        print(area_circulo(radio))
        
           