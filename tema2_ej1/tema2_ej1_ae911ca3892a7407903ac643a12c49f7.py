def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
    pass

def area_rectangulo(base,altura):
    area=base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
    pass

def area_circulo(radio):
    import math
    area=math.pi*(radio**2)
    return area
    pass

if __name__ == "__main__":
    pass
    op=0
    while(op>=1 and op<=4):
        print("Eliga una de las siguiente opciones: ")
        print("(1) Calcular el area de un triangulo")
        print("(2) Calcular el area de un rectangulo")
        print("(3) Calcular el area de un rombo")
        print("(4) Calcular el area de un circulo")
        op=int(input())
    if(op==1):
        base=float(input("Ingrese la base del rectangulo "))
        altura=float(input("Ingrese la altura del rectangulo "))
        print("El área es de:",area_triangulo(base,altura))
    if(op==2):
        base=float(input("Ingrese la base del triangulo "))
        altura=float(input("Ingrese la altura del triangulo "))
        print("El área es de:",area_rectangulo(base,altura))
    if(op==3):
        diagonal1=float(input("Ingrese la diagonal a"))
        diagonal2=float(input("Ingrese la diagonal b "))
        print("El área es de:",area_rombo(diagonal1,diagonal2))
    if(op==4):
        base=float(input("Ingrese el radio "))
        print("El área es de:",area_circulo(radio))