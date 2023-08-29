#Librerias
import math
#Funciones
def area_triangulo(Base,Altura):
    Area = (Base * Altura) / 2
    return(Area)

def area_rectangulo(Base,Altura):
    Area = Base * Altura
    return(Area)

def area_rombo(Diagonal1,Diagonal2):
    Area = (Diagonal1 * Diagonal2) / 2
    return(Area)

def area_circulo(Radio):
    Area = math.pi * (Radio ** 2)
    return (Area)

def menu():
    if __name__ == "__main__":
        print("1. Area triangulo\n2. Area rectangulo\n3. Area rombo\n4. Area circulo")
        menu = int(input("Ingrese numero: "))
        if menu == 1:
            Base = int(input("ingrese la base: "))
            Altura = int(input("ingrese la altura: "))
            print(area_triangulo(Base,Altura))
        elif menu == 2:
            Base = int(input("ingrese la base: "))
            Altura = int(input("ingrese la altura: "))
            print(area_rectangulo(Base,Altura))
        elif menu == 3:
            Diagonal1 = int(input("Ingrese la Diagonal 1: "))
            Diagonal2 = int(input("Ingrese la Diagonal 2: "))
            print(area_rombo(Diagonal1,Diagonal2))
        elif menu == 4:
            Radio = int(input("Ingrese el Radio: "))
            print(area_circulo(Radio))
        else:
            print("Error")
        return ""


print(menu())