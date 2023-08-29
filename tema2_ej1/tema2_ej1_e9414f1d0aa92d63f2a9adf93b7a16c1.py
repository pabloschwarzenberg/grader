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
    print("Bienvenido al programa de cálculo de áreas")
    
    while True:
        print("Seleccione la figura geométrica:")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Rombo")
        print("4. Círculo")
        print("5. Salir")
        
        opcion = int(input("Ingrese el número de la opción deseada: "))
        
        if opcion == 1:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            resultado = area_triangulo(base, altura)
            print("El área del triángulo es:", resultado)
        elif opcion == 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            resultado = area_rectangulo(base, altura)
            print("El área del rectángulo es:", resultado)
        elif opcion == 3:
            diagonal1 = float(input("Ingrese la diagonal 1 del rombo: "))
            diagonal2 = float(input("Ingrese la diagonal 2 del rombo: "))
            resultado = area_rombo(diagonal1, diagonal2)
            print("El área del rombo es:", resultado)
        elif opcion == 4:
            radio = float(input("Ingrese el radio del círculo: "))
            resultado = area_circulo(radio)
            print("El área del círculo es:", resultado)
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
