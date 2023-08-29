import math
def area_triangulo(base,altura):
    pass
    global at
    at=base*altura/2
    return at
def area_rectangulo(base,altura):
    pass
    global are
    are=base*altura
    return are

def area_rombo(diagonal1,diagonal2):
    pass
    global aro
    aro=diagonal1*diagonal2/2
    return aro

def area_circulo(radio):
    pass
    global ac
    ac=radio*radio*math.pi
    return ac


if __name__ == "__main__":
    pass
    menu=int(input("Si desea calcular el area de un triangulo, rectangulo, rombo o circulo, ingrese 1,2,3 o 4 respectivamente"))
    if menu==1:
        base=float(input("ingrese la base"))
        altura=float(input("ingrese la altura"))
        area_triangulo(base,altura)
        print("El area es {0}".format(at))
    if menu==2:
        base=float(input("ingrese la base"))
        altura=float(input("ingrese la altura"))
        area_rectangulo(base,altura)
        print("El area es {0}".format(are))
    if menu==3:
        diagonal1=float(input("ingrese la diagonal 1"))
        diagonal2=float(input("ingrese la diagonal 2"))
        area_rombo(diagonal1,diagonal2)
        print("El area es {0}".format(aro))
    if menu==4:
        radio=float(input("ingrese la radio"))
        area_circulo(radio)
        print("El area es {0}".format(ac))
           