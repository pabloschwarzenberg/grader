import math

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

def area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    # Ejemplo de uso
    base = 11
    altura = 7
    area_tri = area_triangulo(base, altura)
    print("El área del triángulo de base", base, "y altura", altura, "es:", area_tri)

    base = 10
    altura = 6
    area_rect = area_rectangulo(base, altura)
    print("El área del rectángulo de base", base, "y altura", altura, "es:", area_rect)

    diagonal_mayor = 30
    diagonal_menor = 16
    area_rom = area_rombo(diagonal_mayor, diagonal_menor)
    print("El área del rombo con diagonales", diagonal_mayor, "y", diagonal_menor, "es:", area_rom)

    radio = 40
    area_circ = area_circulo(radio)
    print("El área del círculo de radio", radio, "es:", area_circ)

           