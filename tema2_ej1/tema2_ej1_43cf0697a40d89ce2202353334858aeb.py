from math import pi
def area_triangulo(base,altura):
    return (base*altura)/2
    pass

def area_rectangulo(base,altura):
    return base*altura
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
    pass

def area_circulo(radio):
    pi
    return pi*radio**2
    pass

if __name__ == "__main__":
    a = input("Ingrese el Area de la figura que desea calcular:")
    if a == "circulo" or a == "Circulo":
        x = eval(input("Ingrese el radio del circulo"))
        b = area_circulo(x)
        print(b)
    elif a == "rombo" or a == "Rombo":
        x = eval(input("Ingrese la primera diagonal del rombo"))
        y = eval(input("Ingrese la segunda diagonal del rombo"))
        b = area_rombo(x,y)
        print(b)
    elif a == "triangulo" or a == "Triangulo":
        x = eval(input("Ingrese la base del Triangulo"))
        y = eval(input("Ingrese la altura del Triaungulo"))
        b = area_triangulo(x,y)
        print(b)
    elif a == "rectangulo" or a == "Rectangulo":
        x = eval(input("Ingrese la base del rectangulo"))
        y = eval(input("Ingrese la altura del rectangulo"))
        b = area_rectangulo(x,y)
        print(b)
    pass
           