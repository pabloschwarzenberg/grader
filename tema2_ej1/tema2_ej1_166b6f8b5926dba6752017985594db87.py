import math
def area_triangulo(base, altura):
    return base * altura / 2
def area_rectangulo(base, altura):
    return base * altura
def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2
def area_circulo(radio):
    return math.pi * radio ** 2
if __name__ == "__main__":
    base1=int(input("Ingrese la base del triangulo:\n"))
    altura1=int(input("Ingrese la altura del triangulo:\n"))
    base2=int(input("Ingrese la base del rectangulo:\n"))
    altura2=int(input("Ingrese la altura del rectangulo:\n"))
    diagonal1=int(input("Ingrese la diagonal-1 del rombo:\n"))
    diagonal2=int(input("Ingrese la diagonal-2 del rombo:\n"))
    radio1=int(input("Ingrese el radio del rombo:\n"))
    print("Área de triángulo: ")
    print(area_triangulo(base1, altura1))

    print("Área de rectángulo: ")
    print(area_rectangulo(base2, altura2))

    print("Área de rombo: ")
    print(area_rombo(diagonal1, diagonal2))

    print("Área de círculo: ")
    print(area_circulo(radio1))
           