import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    def mostrar_menu():
        print("Seleccione la figura geométrica para calcular su área:")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Rombo")
        print("4. Círculo")

    def obtener_opcion():
        opcion = int(input("Ingrese el número de la opción: "))
        return opcion

    def obtener_valores_rectangulo():
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        return base, altura

    def obtener_valores_triangulo():
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        return base, altura

    def obtener_valores_rombo():
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        return diagonal_mayor, diagonal_menor

    def obtener_valores_circulo():
        radio = float(input("Ingrese el radio del círculo: "))
        return radio

    mostrar_menu()
    opcion = obtener_opcion()

    if opcion == 1:
        base, altura = obtener_valores_rectangulo()
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
    elif opcion == 2:
        base, altura = obtener_valores_triangulo()
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    elif opcion == 3:
        diagonal_mayor, diagonal_menor = obtener_valores_rombo()
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print(f"El área del rombo es: {area}")
    elif opcion == 4:
        radio = obtener_valores_circulo()
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area}")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
