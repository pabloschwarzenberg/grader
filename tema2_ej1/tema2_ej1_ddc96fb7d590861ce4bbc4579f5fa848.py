import math

def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(d1,d2):
    area=d1*d2/2
    return area

def area_circulo(r):
    area=(r**2)*math.pi
    return area

if __name__ == "__main__":
    print("Bienvenido a la Calculadora Geometrica")
    print()
    O=int(input("Ingrese la figura a calcular el Área: 1.Triangulo - 2.Rectangulo - 3.Rombo - 4.Circulo: "))
    if O>4 or O<1:
        print()
        print("Escogiste una opcion invalida, adios por larry")
        print()
    elif O==1:
        B=float(input("Ingrese Base en cm: "))
        H=float(input("Ingrese Altura en cm: "))
        print()
        print("El area es: ",area_triangulo(B,H))
    elif O==2:
        B=float(input("Ingrese Base en cm: "))
        H=float(input("Ingrese Altura en cm: "))
        print()
        print("El area es: ",area_rectangulo(B,H))
    elif O==3:
        B=float(input("Ingrese Diagonal 1 en cm: "))
        H=float(input("Ingrese Diagonal 2 en cm: "))
        print()
        print("El area es: ",area_rombo(B,H))
    elif O==4:
        R=float(input("Ingrese el Radio en cm: "))
        print()
        print("El area es: ",area_circulo(R))
