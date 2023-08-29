import math

def area_triangulo(base,altura):
    A=(base*altura)/2
    return A

def area_rectangulo(base,altura):
    A=base*altura
    return A

def area_rombo(diagonal1,diagonal2):
    A=(diagonal1*diagonal2)/2
    return A

def area_circulo(radio):
    A=math.pi*(radio**2)
    return A

def menu(opcion):
    print("Bienvenido a la Calculadora de Areas")
    if opcion==1:
        base=int(input("Ingrese la Base del Triangulo: "))
        altura=int(input("Ingrese la Altura del Triangulo: "))
        return area_triangulo(base,altura)
    elif opcion==2:
        base=int(input("Ingrese la Base del Rectangulo: "))
        altura=int(input("Ingrese la Altura del Rectangulo: "))
        return area_rectangulo(base,altura)
    elif opcion==3:
        diagonal1=int(input("Ingrese la Primera Diagonal del Rombo: "))
        diagonal2=int(input("Ingrese la Segunda Diagonal del Rombo. "))
        return area_rombo(diagonal1,diagonal2)
    elif opcion==4:
        radio=int(input("Ingrese el Radio del Circulo: "))
        return area_circulo(radio)
  
if __name__ == "__main__":
    opcion=int(input("Ingrese 1, 2, 3 o 4 para calcular el area de un triangulo,rectangulo,rombo o    circulo respectivamente: "))
    menu(opcion)