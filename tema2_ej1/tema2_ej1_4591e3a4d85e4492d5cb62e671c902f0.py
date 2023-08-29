from math import pi
def area_triangulo(base, altura):
    Area=(base*altura)/2
    return Area

def area_rectangulo(base, altura):
    Area=base*altura
    return Area

def area_rombo(diagonal1, diagonal2):
    Area = (diagonal1*diagonal2)/2
    return Area

def area_circulo(radio):
    Area= (radio**2)*pi
    return Area

if __name__ == "__main__":
    while True:
        print("Calculadora Geometrica\n","(1):area_triangulo\n",
        "(2):area_rectangulo\n","(3):area_rombo\n","(4):area_circulo\n", "(5): Salir")
        try:
            opcion=int(input("Seleccione una Opcion: "))
            if opcion==1:
                base=float(input("Ingrese la Base: "))
                altura=float(input("Ingrese la altura: "))
                print(area_triangulo(base,altura))
            elif opcion==2:
                base=float(input("Ingrese la Base: "))
                altura=float(input("Ingrese la altura: "))
                print(area_rectangulo(base,altura))
            elif opcion==3:
                base=float(input("Ingrese la diagonal1: "))
                altura=float(input("Ingrese la diagonal2: "))
                print(area_rombo(base,altura))
            elif opcion==4:
                radio=float(input("Ingrese el radio: "))
                print(area_circulo(radio))
            elif opcion==5:
                break
            else:
                continue
        except:
            continue