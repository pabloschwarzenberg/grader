import math 
def area_triangulo(base,altura):
    area_tria= (base*altura)/2
    return area_tria
    pass

def area_rectangulo(base,altura):
    area_rec=base*altura
    return area_rec
    pass

def area_rombo(diagonal1,diagonal2):
    area_rom=(diagonal1*diagonal2)/2
    return area_rom
    pass

def area_circulo(radio):
    area_cir=math.pi*radio**2
    return area_cir
    pass

if __name__ == "__main__":
    print("Escriba el numero de la opcion que desea usar:")
    print("Area del triángulo, escriba 1")
    print("Area del rectángulo, escriba 2")
    print("Area del rombo, escriba 3")
    print("Area del círculo, escriba 4")
    pregu=int(input(" "))
    if pregu==1:
        base=int(input("Ingrese base del triángulo"))
        altura=int(input("Ingrese altura del triángulo"))
        area=area_triangulo(base,altura)
        print(area) 
    elif pregu==2:
        base=int(input("Ingrese base del rectángulo"))
        altura=int(input("Ingrese altura del rectángulo"))
        area=area_rectangulo(base,altura)
        print(area) 
    elif pregu==3:
        d1=int(input("Ingrese diagonal 1 del rombo"))
        d2=int(input("Ingrese diagonal 2 del rombo"))
        area=area_rombo(d1,d2)
        print(area) 
    elif pregu==4:
        r=int(input("Ingrese radio del círculo"))
        area=area_circulo(r)
        print(area)
    pass
           