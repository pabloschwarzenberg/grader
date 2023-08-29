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
    while True:
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Rombo")
        print("4. Círculo")
        print("5. Salir")
        
        opcion = int(input("Ingresa el número de la figura que deseas calcular el área: "))

        if opcion == 1:
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == 2:
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            area = area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == 3:
            diagonal1 = float(input("Ingresa la longitud de la diagonal 1 del rombo: "))
            diagonal2 = float(input("Ingresa la longitud de la diagonal 2 del rombo: "))
            area = area_rombo(diagonal1, diagonal2)
            print("El área del rombo es:", area)
        elif opcion == 4:
            radio = float(input("Ingresa el radio del círculo: "))
            area = area_circulo(radio)
            print("El área del círculo es:", area)
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intenta nuevamente.")           