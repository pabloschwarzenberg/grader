import math

def area_triangulo(base,altura):
    area = base*altura/2
    return area
    pass

def area_rectangulo(base,altura):
    area = base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area
    pass

def area_circulo(radio):
    area = math.pi*radio**2
    return area
    pass

if __name__ == "__main__":
    menu = ""
    while menu!=5:
        print("\nBienvenido a tu calculadora")
        print("1-Areá del triángulo")
        print("2-Areá del rectángulo")
        print("3-Areá del rombo")
        print("4-Areá del círculo")
        print("5-Salir")
        menu = int(input("Ingrese un número: "))
        if menu==1:
            base = int(input("Ingrese la base: "))
            altura = int(input("Ingrese la altura: "))
            trianarea = area_triangulo(base,altura)
            print("El área del triángulo es",trianarea)
        elif menu==2:
            base = int(input("Ingrese la base: "))
            altura = int(input("Ingrese la altura: "))
            rectanarea = area_rectangulo(base,altura)
            print("El área del rectángulo es",rectanarea)
        elif menu==3:
            diagonal1 = int(input("Ingrese el primer diagonal: "))
            diagonal2 = int(input("Ingrese el segundo diagonal: "))
            rombonarea = area_rombo(diagonal1,diagonal2)
            print("El área del rombo es",rombonarea)
        elif menu==4:
            radio = int(input("Ingrese el radio: "))
            circunarea = area_circulo(radio)
            print("El área del círculo es",circunarea)
        elif menu==5:
            print("Saliendo")
            break
    pass
           