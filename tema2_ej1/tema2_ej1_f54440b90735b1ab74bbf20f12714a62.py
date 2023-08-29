def area_triangulo(base, altura):
    area_tri = (base * altura) / 2.0
    return area_tri

def area_rectangulo(base, altura):
    area_rec = base * altura
    return area_rec

def area_rombo(diagonal1, diagonal2):
    area_rom = (diagonal1 * diagonal2) / 2.0
    return area_rom

def area_circulo(radio):
    import math
    area_cir = math.pi * (radio ** 2)
    return area_cir

if __name__ == "__main__":
    c = input("Que area desea calcular, triangulo, rectangulo, rombo o circulo: ")
    
    if c == "triangulo":
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(area_triangulo(base, altura))
    elif c == "rectangulo":
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(area_rectangulo(base, altura))
    elif c == "rombo":
        diagonal1 = int(input("Ingrese la diagonal 1: "))
        diagonal2 = int(input("Ingrese la diagonal 2: "))
        print(area_rombo(diagonal1, diagonal2))
    elif c == "circulo":
        radio = int(input("Ingrese el radio: "))
        print(area_circulo(radio))
           