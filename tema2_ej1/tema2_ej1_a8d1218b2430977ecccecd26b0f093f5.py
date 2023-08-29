import math
def area_triangulo(base,altura):
    return (base*altura) / 2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print(f"1. Area triangulo.\n2. Area rectangulo.\n3. Area rombo.\n4. Area ciruclo.")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(f"Area del triangulo: {area_triangulo(base,altura)}")
    elif opcion == 2:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(f"Area del rectangulo: {area_rectangulo(base,altura)}")
    elif opcion == 3:
        diagonal1 = int(input("Ingrese primera diagonal: "))
        diagonal2 = int(input("Ingrese segunda diagonal: "))
        print(f"Area del rombo: {area_rombo(diagonal1,diagonal2)}")
    elif opcion == 4:
        radio = int(input("Ingrese radio: "))
        print(f"Area del circulo: {area_circulo(radio)}")
    else:
        print("Opción inexistente...")

           