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
    area=(math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    print("Elija una figura geométrica para calcular su área:")
    print("1) Triángulo")
    print("2) Rectángulo")
    print("3) Rombo")
    print("4) Círculo")
    opcion=int(input("Elección: "))
    if opcion==1:
        dato1=int(input("Base: "))
        dato2=int(input("Altura: "))
        print("El área es:")
        print(area_triangulo(dato1,dato2))
    if opcion==2:
        dato1=int(input("Base: "))
        dato2=int(input("Altura: "))
        print("El área es:")
        print(area_rectangulo(dato1,dato2))
    if opcion==3:
        dato1=int(input("Diagonal 1: "))
        dato2=int(input("Diagonal 2: "))
        print("El área es:")
        print(area_rombo(dato1,dato2))
    if opcion==4:
        dato=int(input("Radio: "))
        print("El área es:")
        print(area_circulo(dato))
           