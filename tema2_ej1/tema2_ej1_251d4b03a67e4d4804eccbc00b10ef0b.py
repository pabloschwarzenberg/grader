from math import pi
def area_triangulo(b, h):
    a = (b*h)/2
    return a

def area_rectangulo(b, h):
    a = b*h
    return a

def area_rombo(diagonal1, diagonal2):
    a = (diagonal1*diagonal2)/2
    return a

def area_circulo(radio):
    a = (pi*radio**2)
    return a

if __name__ == "main":
    print("Menu")
    figura = input("Ingrese la figura que desea calcular: ")

    if figura != "rectangulo" and figura != "triangulo" and figura != "rombo" and figura != "circulo":
        print("INCORRECTO")
        exit()

    elif figura == "triangulo":
        b = float(input("Ingrese la base: "))
        h = float(input("Ingrese la altura: "))
        print(area_triangulo)
    elif figura == "rectangulo":
        b = float(input("Ingrese la base"))
        h = float(input("Ingrese la altura"))
        print(area_rectangulo)
    elif figura == "circulo":
        radio = float(input("Ingrese el radio: "))
        print(area_circulo(radio))
    elif figura == "rombo":
        diagonal_1 = float(input("Ingrese diagonal que es mayor: "))
        diagonal_2 = float(input("Ingrese diagonal que es menor: "))
        print(area_rombo(diagonal_1, diagonal_2))
    
    
    