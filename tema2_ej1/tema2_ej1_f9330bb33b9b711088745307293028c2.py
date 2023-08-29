import math

def area_triangulo(base,altura):
    areaT=(base*altura)/2
    return areaT

def area_rectangulo(base,altura):
    areaC=base*altura
    return areaC

def area_rombo(diagonal1,diagonal2):
    areaR=(diagonal1*diagonal2)/2
    return areaR

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area

if __name__=="__main__":
    v = True
    while v:
        print("\tMenu\n1. Area triangulo\n2. Area Rectangulo\n3. Area Rombo\n4. Area Ciruclo\n5. Salir")
        Opcion = input("Ingrese opcion: ")
        if Opcion == "1":
            print("Area del triangulo")
            base = int(input("Ingrese la base:"))
            altura = int(input("Ingrese la altura:"))
            Area = area_triangulo(base,altura)
            print("Area del triangulo : "+ str(Area))
        elif Opcion == "2":
            print("Area del rectangulo")
            base = int(input("Ingrese la base:"))
            altura = int(input("Ingrese la altura:"))
            Area = area_rectangulo(base,altura)
            print("Area del rectangulo : "+ str(Area))
        elif Opcion == "3":
            print("Area del rombo")
            diagonal1 = int(input("Ingrese la diagonal 1:"))
            diagonal2 = int(input("Ingrese la diagonal 2:"))
            Area = area_rombo(diagonal1,diagonal2)
            print("Area del rombo : "+ str(Area))
        elif Opcion == "4":
            print("Area del circulo")
            radio = int(input("Ingrese el radio:"))
            Area = area_circulo(radio)
            print("Area del circulo :"+ str(Area))
        elif Opcion == "5":
            v = False
            print("Fin del programa")
        else:
            print("Ingrese opcion valida")