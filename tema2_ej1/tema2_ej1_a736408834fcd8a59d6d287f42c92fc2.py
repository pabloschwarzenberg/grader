import math

def area_triangulo(base, altura):
    area_t = (base * altura) / 2
    return area_t

def area_rectangulo(base, altura):
    area_r = base * altura
    return area_r

def area_rombo(diagonal1, diagonal2):
    area_ro = (diagonal1 * diagonal2) / 2
    return area_ro

def area_circulo(radio):
    area_c = math.pi * radio**2
    return area_c

if __name__ == "__main__":
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    diagonal1 = int(input("Ingrese la diagonal 1: "))
    diagonal2 = int(input("Ingrese la diagonal 2: "))
    radio = int(input("Ingrese el radio: "))

    areas = {
        "Triángulo": area_triangulo(base, altura),
        "Rectángulo": area_rectangulo(base, altura),
        "Rombo": area_rombo(diagonal1, diagonal2),
        "Círculo": area_circulo(radio)
    }

    for figura, area in areas.items():
        print("El área del ",{figura}," es: ",{area})
