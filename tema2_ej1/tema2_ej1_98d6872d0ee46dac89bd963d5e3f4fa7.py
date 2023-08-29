import math

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    print("1. Calcular área del rectángulo")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del rombo")
    print("4. Calcular área del círculo")
    
    opcion = int(input("Ingrese el número correspondiente a la figura que desea calcular: "))
    
    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area_rectangulo)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area_triangulo = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area_triangulo)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
        area_rombo = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area_rombo)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print("El área del círculo es:", area_circulo)
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
