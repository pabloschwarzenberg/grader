import math
def area_triangulo(base,altura):
    area=float(base*altura/2)
    return area
    pass

def area_rectangulo(base,altura):
    area=float(base*altura)
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area=float(diagonal1*diagonal2/2)
    return area
    pass

def area_circulo(radio):
    area=math.pi*radio**2
    return area
    pass

if __name__ == "__main__":
    print("1)Triángulo")
    print("2)Rectángulo")
    print("3)Rombo")
    print("4)Círculo")
    eleccion=int(input("Elige una figura: "))
    if eleccion==1:
        a=int(input("Agrega la base: "))
        b=int(input("Agrega la altura: "))
        print("El área es ",area_triangulo(a,b))
    elif eleccion==2:
        a=int(input("Agrega la base: "))
        b=int(input("Agrega la altura: "))
        print("El área es ",area_rectangulo(a,b))
    elif eleccion==3:
        a=int(input("Agrega una diagonal: "))
        b=int(input("Agrega otra diagonal: "))
        print("El área es ",area_rombo(a,b))
    elif eleccion==4:
        a=int(input("Agrega el radio: "))
        print("El área es ",area_circulo(a))
    pass
           