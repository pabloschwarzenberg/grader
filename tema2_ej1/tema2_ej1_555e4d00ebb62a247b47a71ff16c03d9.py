import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_triangulo(base, altura):
    return 0.5 * base * altura

if __name__ == "__main__":
    import modulo  # Replace "modulo" with the actual name of your module
    base = 11
    altura = 7
    ae1 = 38.5
    
    if ae1 != modulo.area_triangulo(base, altura):  # Use the correct name of the function
        print("El área del triángulo es diferente")
    else:
        print("El área del triángulo es igual")