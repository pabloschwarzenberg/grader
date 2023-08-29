from math import pi
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = pi * radio**2
    return area
if __name__ == "__main__":
    opcion = -1
    while(opcion > 4 or opcion < 0):
        print("Menú de cálculo de área")
        print("0.Área triangulo")
        print("1.Área rectangulo")
        print("2.Área rombo")
        print("3.Área circulo")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 0:
            area_triangulo(int(input("Ingresa la base: ")),int(input("Ingresa la altura: ")))
        elif(opcion == 1):
            area_rectangulo(int(input("Ingresa la base: ")),int(input("Ingresa la altura: ")))
        elif(opcion == 2):
            area_rombo(int(input("Ingresa la diagonal 1: ")),int(input("Ingresa la diagonal 2: ")))
        else:           
            area_circulo(int(input("Ingresa el radio: ")))

    pass
           