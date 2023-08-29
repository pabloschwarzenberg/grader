import math

def area_triangulo(base,altura):
    area = base * altura * 0.5
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2 * 0.5
    return area

def area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    quiero = input("""¿De qué figura quieres su área?
1) Triángulo
2) Rectángulo
3) Rombo
4) Círculo
""")
    if quiero == "1":
        base = int(input("Dame la base: "))
        altura = int(input("Dame la altura: "))
        print("El área es ",area_triangulo(base,altura))
    elif quiero == "2":
        base = int(input("Dame la base: "))
        altura = int(input("Dame la altura: "))
        print("El área es ",area_rectangulo(base,altura))
    elif quiero == "3":
        d1 = int(input("Dame la diagonal 1: "))
        d2 = int(input("Dame la diagonal 2: "))
        print("El área es ", area_rombo(d1,d2))
    elif quiero == "4":
        radio = int(input("Dame el radio: "))
        print("El área es ",area_circulo(radio))
    else:
        print("respuesta no válida")