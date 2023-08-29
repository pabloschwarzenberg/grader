import math

def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return math.pi*(radio**2)

if __name__ == "__main__":
    figura=input("¿El área de que figura desea calcular?(1=Triangulo, 2=Rectangulo, 3=Rombo, 4=Circulo)")
    if figura==1:
        base=eval(input("Ingrese la base de la figura:"))
        altura=eval(input("Ingrese la altura de la figura:"))
        print("El area del triangulo es {}:".format(area_triangulo))
    elif figura==2:
        base=eval(input("Ingrese la base de la figura:"))
        altura=eval(input("Ingrese la altura de la figura:"))
        print("El area del rectangulo es {}:".format(area_rectangulo))
    elif figura==3:
        diagonal1=eval(input("Ingrese la diagonal 1 de la figura:"))
        diagonal2=eval(input("Ingrese la diagonal 2 de la figura:"))
        print("El area del rombo es {}:".format(area_rombo))
    elif figura==4:
        radio=eval(input("Ingrese el radio del circulo:"))
        print("El area del circulo es {}:".format(area_circulo))
    