import math
def area_triangulo(base,altura):
    area= base*altura/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area= diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area= math.pi*radio**2
    return area

if __name__ == "__main__":
    print("(1)Calcular área del triángulo\n(2)Calcular área del rectangulo\n(3)Calcular área del rombo\n(4)Calcular área del círculo")
    opcion= int(input("ingrese una opcion del menu: "))
    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area_triangulo = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area_triangulo)
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area_rectangulo)
    elif opcion == 3:
        diagonal1 = float(input("ingrese una diagonal del rombo: "))
        diagonal2 = float(input("ingrese la otra diagonal del rombo: "))
        area_rombo = calcular_area_rombo(diagonal1, diagonal2)
        print("el área del rombo es: ", area_rombo)
    elif opcion==4:
        radio = float(input("Ingrese el radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print("El área del círculo es:", area_circulo)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
           