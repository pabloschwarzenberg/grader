from math import pi
 
def area_triangulo(base,altura):
    return base*altura/2
 
def area_rectangulo(base,altura):
    return base*altura
 
def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2
 
def area_circulo(radio):
    return pi*radio**2
 
if __name__ == "__main__":
    print("Que deseas hacer?")
    print("1 = Area Triangulo")
    print("2 = Area Rectangulo")
    print("3 = Area Rombo")
    print("4 = Area Circulo")
    respuesta = input("> ")
    if respuesta == "1":
        print(area_triangulo(int(input("Base: ")),int(input("Altura: "))))
    if respuesta == "2":
        print(area_rectangulo(int(input("Base: ")),int(input("Altura: "))))
    if respuesta == "3":
        print(area_rombo(int(input("Diagnoal 1: ")),int(input("Diagonal 2: "))))
    if respuesta == "4":
        print(area_circulo(int(input("Radio: "))))