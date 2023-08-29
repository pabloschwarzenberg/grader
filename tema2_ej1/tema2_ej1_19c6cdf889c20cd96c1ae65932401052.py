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


import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("Calculadora Geométrica")
    print("----------------------")
    print("1. Calcular área de un triángulo")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un rombo")
    print("4. Calcular área de un círculo")
    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 3:
        diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
        area = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")
        
#FIN
