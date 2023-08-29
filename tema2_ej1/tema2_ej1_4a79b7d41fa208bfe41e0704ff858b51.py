import math

def area_triangulo(base,altura):
    area=(altura*base)/2
    return area

def area_rectangulo(base,altura):
    area=altura*base
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=math.pi*radio**2
    return area

#funcion principal
if __name__ == "__main__":
    opcionMenu=int(input("Ingrese un numero entre 1-4 para encontrar area deseada:(1) triangulo, (2) rectangulo, (3) rombo, (4) circulo: "))
    if opcionMenu == 1:
        base = int(input("Ingrese valor numerico de la base: "))
        altura = int(input("Ingrese valor numerico de la altura: "))
        print (area_triangulo(base,altura))
    elif opcionMenu == 2:
        base = int(input("Ingrese valor numerico de la base: "))
        altura = int(input("Ingrese valor numerico de la altura: "))
        print(area_rectangulo(base, altura))
    elif opcionMenu == 3:
        diagonal1=int(input("Ingrese valor numerico de la diagonal1: "))
        diagonal2=int(input("Ingrese valor numerico de la diagonal2: "))
        print(area_rombo(diagonal1,diagonal2))
    elif opcionMenu==4:
        radio=int(input("Ingrese valor numerico para el radio:"))
        print(area_circulo(radio))
    else:
        print("Opcion invalida. No se puede proceder a calcular area.")
