import math

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return 0.5 * base * altura

# Función para calcular el área de un rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio**2

# Función para mostrar el menú y recibir la opción del usuario
def menu():
    print("Seleccione la figura geométrica a calcular:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    opcion = input("Ingrese su opción (1-4): ")
    return opcion

# Función principal que llama a la función correspondiente según la opción del usuario
def calcular_area(opcion):
    if opcion == "1":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
    elif opcion == "2":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
    elif opcion == "3":
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        resultado = area_rombo(diagonal_mayor, diagonal_menor)
    elif opcion == "4":
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = area_circulo(radio)
    else:
        print("Opción inválida.")
        resultado = None
    
    if resultado:
        print("El área es: {}".format(resultado))

if __name__ == "__main__":
    opcion = menu()
    calcular_area
