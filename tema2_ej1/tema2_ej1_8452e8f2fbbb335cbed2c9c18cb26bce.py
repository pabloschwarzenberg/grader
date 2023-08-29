from math import pi
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = (base*altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area = pi*(radio**2)
    return area

if __name__ == "__main__":
    print("Calculadora Geométrica\n"
          "1.- Área de triángulo\n"
          "2.- Área rectángulo\n"
          "3.- Área rombo\n"
          "4.- Área círculo\n")
    x = int(input("Para realizar alguna operación eliga una opción: "))
    while x < 1 or x > 4:
        x = int(input("Para realizar alguna operación eliga una opción dentro del rango por favor: "))
    if x == 1:
        b = float(input("Ingrese la base del triángulo: "))
        a = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es",area_triangulo(b,a))
    elif x == 2:
        l = float(input("Ingrese el largo del rectángulo: "))
        a = float(input("Ingrese el ancho del rectángulo: "))
        print("El área del rectángulo es",area_rectangulo(l,a))
    elif x == 3:
        d1 = float(input("Ingrese la primera diagonal del rombo: "))
        d2 = float(input("Ingrese la segunda diagonal del rombo: "))
        print("El área del rombo es",area_rombo(d1,d2))
    else:
        r = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es",round(area_circulo(r),2))