import math
def area_triangulo(base,altura):
    x=(base*altura)/2
    return x
    pass

def area_rectangulo(base,altura):
    x=base*altura
    return x
    pass

def area_rombo(diagonal1,diagonal2):
    x=(diagonal1*diagonal2)/2
    return x
    pass

def area_circulo(radio):
    x=math.pi*(radio**2)
    return x
    pass

def menu():
    opcion=0
    while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4:
        opcion = 1
    return opcion
if __name__ == "__main__":
    s=menu()
    if s==1:
        base=11
        altura=7
        area_triangulo(base,altura)
    elif s==2:
        base=10
        altura=6
        area_rectangulo(base,altura)
    elif s==3:
        diagonal1=30
        diagonal2=16
        area_rombo(diagonal1,diagonal2)
    elif s==4:
        radio=40
        area_circulo(radio)
    pass