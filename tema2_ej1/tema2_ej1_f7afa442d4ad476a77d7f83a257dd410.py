from math import pi
def area_triangulo(base, altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base, altura):
    area = base*altura
    return area

def area_rombo(diagonal1, diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = (pi*radio**2)
    return area

if __name__ == "__main__":
    print("Menu")
    figura = input("Ingrese la figura que desea calcular: ")

    if figura != "triangulo" and figura != "rectangulo" and figura != "rombo" and figura != "circulo":
        print("Mecanismo anti estupidos: activado")
        exit()

    if figura == "triangulo":
        base = float(input("Ingrese base: "))
        altura = float(input("Ingrese altura: "))
        print(area_triangulo)
    if figura == "rectangulo":
        base = float(input("Ingrese base"))
        altura = float(input("Ingrese altura"))
        print(area_rectangulo)
    if figura == "circulo":
        radio = float(input("Ingrese radio: "))
        print(area_circulo(radio))
    if figura == "rombo":
        diagonal_1 = float(input("Ingrese diagonal mayor: "))
        diagonal_2 = float(input("Ingrese diagonal menor: "))
        print(area_rombo(diagonal_1, diagonal_2))


