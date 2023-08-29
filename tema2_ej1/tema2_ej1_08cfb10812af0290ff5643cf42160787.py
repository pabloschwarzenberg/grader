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
    import math
    area=math.pi*radio**2
    return area

if __name__ == "__main__":
    l=["Calcular area de triangulo (1)","Calcular area de rectangulo (2)","Calcular area de rombo (3)","Calcular area de circulo (4)"]
    print(l)
    elegir=int(input())
    if elegir==1:
        base=int(input("Ingrese Base"))
        altura=int(input("Ingrese altura"))
        print(area_triangulo(base,altura))
    elif elegir==2:
        base=int(input("Ingrese Base"))
        altura=int(input("Ingrese altura"))
        print(area_rectangulo(base,altura))
    elif elegir==3:
        diagonal1=int(input("Ingrese diagonal1"))
        diagonal2=int(input("diagonal2"))
        print(area_rombo(diagonal1,diagonal2))
    elif elegir==4:
        radio=int(input("radio"))
        print(area_circulo(radio))