def area_triangulo(base,altura):

    At = (base * altura)/2

def area_rectangulo(base,altura):

    Arect = base * altura

def area_rombo(diagonal1,diagonal2):

    Arom = (diagonal1 * diagonal2)/2

def area_circulo(radio):

    import math
    Ac = math.pi * (radio)^2

if __name__ == "__main__":

    base = float(input("Ingrese base: "))
    altura = float(input("Ingrese altura: "))
    diagonal1 = float(input("Ingrese primera diagonal: "))
    diagonal2 = float(input("Ingrese segunda diagonal: "))
    radio = float(input("Ingrese radio: "))

    if area_triangulo(base, altura):
        
        float(print("El area del triangulo es {0}".format(At)))

    if area_rectangulo(base,altura):

        float(print("El area del rectanglo es {0}".format(area_rectangulo)))

    if area_rombo(diagonal1,diagonal2):

        float(print("El area del rombo es {0}".format(area_rombo)))

    if area_circulo(radio):

        float(print("El area del circulo es {0}".format(area_circulo)))

