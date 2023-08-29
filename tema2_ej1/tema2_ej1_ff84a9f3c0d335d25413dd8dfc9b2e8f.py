import math
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
    area=math.pi*(radio)**2
    return area

if __name__ == "__main__":
    figura=int(input("""    (1) Triángulo
    (2) Rectángulo
    (3) Rombo
    (4) Círculo
    Selecciona la figura la cual quieres calcular el área: """))

    if figura==1:
        base=int(input("Ingrese la base del triángulo: "))
        altura=int(input("Ingrese la altura del triángulo: "))
        print(area_triangulo(base,altura))
    if figura==2:
        base=int(input("Ingrese la base del rectángulo: "))
        altura=int(input("Ingrese la altura del rectángulo: "))
        print(area_rectangulo(base,altura))
    if figura==3:
        diagonal1=int(input("Ingrese una diagonal del rombo: "))
        diagonal2=int(input("Ingrese la otra diagonal del rombo: "))
        print(area_rombo(diagonal1,diagonal2))
    if figura==4:
        radio=int(input("Ingrese el radio del circulo: "))
        print(area_circulo(radio))           