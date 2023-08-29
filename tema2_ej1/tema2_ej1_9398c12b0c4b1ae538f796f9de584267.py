def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    import math
    return radio*radio*(math.pi) 

if __name__ == "__main__":
    print("(1)Area de un triangulo")
    print("(2)Area de un rectangulo")
    print("(3)Area de un rombo")
    print("(4)Area de un circulo")
    q=int(input("¿que quiere calcular?"))
    if q==1:
        base=float(input("Base:"))
        altura=float(input("Altura:"))
        print("EL area del triangulo es:",area_triangulo(base,altura))
    elif q==2:
        base=float(input("Base:"))
        altura=float(input("Altura:"))
        print("EL area del rectangulo es:",area_rectangulo(base,altura))
    elif q==3:
        diagonal1=float(input("Diagonal 1:"))
        diagonal2=float(input("Diagonal 2:"))
        print("EL area del rombo es:",area_rombo(diagonal1,diagonal2))
    elif q==4:
        radio=float(input("Radio:"))
        print("EL area del circulo es:",area_circulo(radio))
    