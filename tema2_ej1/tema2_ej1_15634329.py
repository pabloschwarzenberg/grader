import math
def area_triangulo(base,altura):
    return (base*altura)/2
    pass

def area_rectangulo(base,altura):
    return base*altura
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
    pass

def area_circulo(radio):
    return (radio**2)*math.pi
    pass


#if __name__ == "__main__":
    S=int(input("De que figura buscas el area(1,2,3,4)"))
    if S==1:
        L=(input("Ingrese base y altura (base,altura)")).split(",")
        A=area_triangulo(int(L[0]),int(L[1]))
    elif S==2:
        L=(input("Ingrese base y altura (base,altura)")).split(",")
        A=area_rectangulo(int(L[0]),int(L[1]))
    elif S==3:
        L=(input("Ingrese diagonal1,diagonal2")).split(",")
        A=area_rombo(int(L[0]),int(L[1]))
    elif S==4:
        radio=input("Ingrese radio")
        A=area_circulo(int(radio))
    print(A)