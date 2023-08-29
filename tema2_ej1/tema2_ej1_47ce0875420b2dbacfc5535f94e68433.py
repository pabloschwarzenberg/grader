import math
def area_triangulo(base,altura):
    return((base*altura)/2)
    pass
def area_rectangulo(base,altura):
    return(base*altura)
    pass
def area_rombo(diagonal1,diagonal2):
    return((diagonal1*diagonal2)/2)
    pass
def area_circulo(radio):
    return(math.pi*radio*radio)
    pass
if __name__ == "__main__":
    fig=input("Elija a que figura le desea calcular su área:\n1)Triangulo \n2)Rectangulo \n3)Rombo \n4)Circulo \n=")
    if fig=="1":
        print("Ingrese el valor de: ")
        h=float(input("-La altura= "))
        b=float(input("-La base= "))
        resultado=area_triangulo(b,h)
        print(resultado)
    elif fig=="2":
        print("Ingrese el valor de: ")
        h=float(input("-La altura= "))
        b=float(input("-La base= "))
        resultado=area_rectangulo(b,h)
        print(resultado)
    elif fig=="3":
        print("Ingrese el valor de: ")
        d1=float(input("-Diagonal mayor= "))
        d2=float(input("-Diagonal menor= "))
        resultado=area_rombo(d1,d2)
        print(resultado)
    elif fig=="4":
        r=float(input("Ingrese el valor del radio= "))
        resultado=area_circulo(r)
        print(resultado)
    pass