def area_triangulo(base,altura):
    area = base*altura/2
    pass
    return area

def area_rectangulo(base,altura):
    area = base*altura
    pass
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    pass
    return area

def area_circulo(radio):
    from math import pi
    area = pi*(radio**2)
    pass
    return area

if __name__ == "__main__":
    a=str(input("¿A qué figura desea calcularle el área: triangulo, rectangulo, rombo o circulo?\n"))
    if a in ("rectangulo","triangulo","rombo","circulo"):
        if a == "rectangulo":
            base = float(input("¿Cuál es su base?\n"))
            altura = float(input("¿Cuál es su altura?\n"))
            print(area_rectangulo(base,altura))
        if a == "triangulo":
            base = float(input("¿Cuál es su base?\n"))
            altura = float(input("¿Cuál es su altura?\n"))
            print(area_triangulo(base,altura))
        if a == "rombo":
            d1 = float(input("¿Cuál es su primera diagonal?\n"))
            d2 = float(input("¿Cuál es su segunda diagonal?\n"))
            print(area_rombo(d1,d2))
        if a == "circulo":
            radio = float(input("¿Cuál es su radio?\n"))
            print(area_circulo(radio))
    else:
        print("Entrada invalida, trate de nuevo")
    pass
           