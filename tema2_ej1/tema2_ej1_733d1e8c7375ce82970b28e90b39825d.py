from math import pi
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=pi*(radio**2)
    return area

if __name__ == "__main__":
    print("¿Qué desea calcular?","\n",
          "1: Área de un triángulo.","\n",
          "2: Área de un rectángulo.","\n",
          "3: Área de un rombo.","\n",
          "4: Área de un círculo.","\n")
    figura=input("Respuesta: ")

    if  figura=="1":
        base=float(input("Ingrese base del triángulo: "))
        altura=float(input("Ingrese altura del triángulo: "))
        area_triangulo(base,altura)

    elif figura=="2":
        base=float(input("Ingrese base del rectángulo: "))
        altura=float(input("Ingrese altura rectángulo: "))
        area_rectangulo(base,altura)

    elif figura=="3":
        diagonal1=float(input("Ingrese diagonal N°1: "))
        diagonal2=float(input("Ingrese diagonal N°2: "))
        print(area_rombo(diagonal1,diagonal2))
        
    elif figura=="4":
        radio=float(input("Ingrese el radio del círculo: "))
        area_circulo(radio)