import math
def area_triangulo(base,altura):
    return (base * altura) / 2
    pass

def area_rectangulo(base,altura):
    return base * altura
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2) / 2
    pass

def area_circulo(radio):
    return math.pi * radio**2
    pass

if __name__ == "__main__":
    opcion = int(input("Ingrese la figura a calcular (1 - Rectángulo, 2 - Triángulo, 3 - Rombo, 4 - Círculo): "))
    
    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))
        
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
        
    elif opcion == 3:
        diagonal_larga = float(input("Ingrese la diagonal larga del rombo: "))
        diagonal_corta = float(input("Ingrese la diagonal corta del rombo: "))
        print("El área del rombo es:", area_rombo(diagonal_larga, diagonal_corta))
        
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
        
    else:
        print("La opción ingresada no es válida.")
    pass
           