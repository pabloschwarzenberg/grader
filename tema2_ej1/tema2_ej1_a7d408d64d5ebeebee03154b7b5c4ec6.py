import math

def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=math.pi*radio*radio
    return area

if __name__ == "__main__":
    print("¿Qué área desea calcular?:")
    print(" a)Triángulo \n b)Rectángulo \n c)Rombo \n d)Circulo")
    r=input()
    if r=='a':
        base=int(input())
        altura=int(input())
        A=area_triangulo(base,altura)
        print(A)
    elif r=='b':
        base=int(input())
        altura=int(input())
        A=area_rectangulo(base,altura)
        print(A)
    elif r=='c':
        diagonal1=int(input())
        diagonal2=int(input())
        A=area_rombo(diagonal1,diagonal2)
        print(A)
    elif r=='d':
                      radio=int(input())
                      A=area_circulo(radio)
                      print(A)