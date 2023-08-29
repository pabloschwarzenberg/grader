import math

area=0

def area_triangulo(Base,Altura):
    area=(Base*Altura)/2
    return area

def area_rectangulo(Base,Altura):
    area=Base*Altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=(math.pi*(radio**2))
    return area

if __name__ == "__main__":
    select=input("Por favor coloca la figura del cual quiere calcular su area (T - triangulo; R - rectangulo; O - rombo; C - circulo): ")
    if select == "T" or select == "t":
        input1=int(input("coloca la Base: "))
        input2=int(input("coloca la Altura: "))
        print("El area del triangulo es: ", area_triangulo(input1,input2))
    elif select == "R" or select == "r":
        input1=int(input("coloca la Base: "))
        input2=int(input("coloca la Altura: "))
        print("El area del rectangulo es: ", area_rectangulo(input1,input2))
    elif select == "O" or select == "o":
        input1=int(input("coloca la diagonal 1: "))
        input2=int(input("coloca la diagonal 2: "))
        print("El area del rombo es: ", area_rombo(input1,input2))
    elif select == "C" or select == "c":
        input1=int(input("coloca el radio del circulo: "))
        print("El area del circulo es: ", area_circulo(input1))