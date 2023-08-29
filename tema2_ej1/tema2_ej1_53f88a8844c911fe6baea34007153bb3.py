import math
def area_triangulo(base,altura):
    area=int(base)*int(altura)/2
    return area

def area_rectangulo(base,altura):
    area=int(base)*int(altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area=int(diagonal1)*int(diagonal2)*1/2
    return area

def area_circulo(radio):
    area=math.pi*math.pow(int(radio),2)
    return area

if __name__=="__main__":
    print("(1) Triangulo\n"
          "(2) Rectangulo\n"
          "(3) Rombo\n"
          "(4) Circulo")

    numero=int(input("Selecciones: "))
    if numero==1:
        base=input("Ingrese la base: ")
        altura=input("Ingrese la altura: ")
        print(area_triangulo(base,altura))
    elif numero==2:
        base=input("Ingrese la base: ")
        altura=input("Ingrese la altura: ")
        print(area_rectangulo(base,altura))
    elif numero==3:
        diagonal1=input("Ingrese la diagonal1: ")
        diagonal2=input("Ingrese la diagonal2: ")
        print(area_rombo(diagonal1,diagonal2))
    elif numero==4:
        radio=input("Ingrese el radio: ")
        print(area_circulo(radio))