import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    print("Calculadora de áreas")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    opcion = int(input("Seleccionar figura para calcular el área (1/2/3/4): "))

    if opcion == 1:
        base = float(input("Ingresar la base del rectángulo: "))
        altura = float(input("Ingresar la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        
    elif opcion == 2:
        base = float(input("Ingresar la base del triángulo: "))
        altura = float(input("Ingresar la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        
    elif opcion == 3:
        diagonal_mayor = float(input("Ingresar la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresar la diagonal menor del rombo: "))
        resultado = area_rombo(diagonal_mayor, diagonal_menor)
        
    elif opcion == 4:
        radio = float(input("Ingresar el radio del círculo: "))
        resultado = area_circulo(radio)
        
    else:
        print("Opción inválida.Seleccione una opción válida.")
