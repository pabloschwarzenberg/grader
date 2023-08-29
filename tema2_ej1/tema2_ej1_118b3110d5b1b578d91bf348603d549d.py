from math import pi
def area_triangulo(base,altura):
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area = pi*(radio**2)
    return area

if __name__ == "__main__":
    print("0: Área triángulo")
    print("1: Área Rectángulo")
    print("2: Área Rombo")
    print("3: Área Círculo")
    op = int(input("Seleccione una operación:"))
    if op == 0:
        base = float(input("Ingrse la base:"))
        altura = float(input("Ingrse la altura:"))
        area = area_triangulo(base,altura)
    elif op == 1:
        base = float(input("Ingrse la base:"))
        altura = float(input("Ingrse la altura:"))
        area = area_rectangulo(base,altura)
    elif op == 2:
        diagonal1 = float(input("Ingrse una diagonal:"))
        diagonal2 = float(input("Ingrse la otra diagonal:"))
        area = area_rombo(diagonal1,diagonal2)
    elif op == 3:
        radio = float(input("Ingrse el radio:"))
        area = area_circulo(radio)