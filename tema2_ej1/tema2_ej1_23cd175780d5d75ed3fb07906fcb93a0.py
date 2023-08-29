from math import pi
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
    A=pi*radio**2
    return A

if __name__ == "__main__":
    #menu
    print(" Menú ")
    print(" 1. Área de un triángulo ")
    print(" 2. Área de un rectángulo ")
    print(" 3. Área de un rombo ")
    print(" 4. Área de un circulo ")
    opcion=int(input("Ingrese una opcion a calcular : "))
    
    if opcion==1:
        b=float(input("Ingrese la base del trángulo: "))
        h=float(input("Ingrese la altura del triángulo: "))
        print(area_triangulo(b,h))
    elif opcion==2:
        a=float(input("Ingrese la base del rectangulo: "))
        c=float(input("Ingrese la altura del rectangulo: "))
        print(area_rectangulo(a,c))
    elif opcion==3:
        d1=float(input("Ingrese la diagonal 1: "))
        d2=float(input("Ingrese la diagonal 2: "))
        print(area_rombo(d1,d2))
    elif opcion==4:
        r=float(input("Ingrese el radio del circulo: "))
        print(area_circulo(r))

