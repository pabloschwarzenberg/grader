import math
def area_triangulo(base,altura):
    return(base*altura)/2
def area_rectangulo(base,altura):
    return(base*altura)
def area_rombo(diagonal1,diagonal2):
    return(diagonal1*diagonal2)/2
def area_circulo(radio):
    return(math.pi*radio**2)
if __name__ == "__main__":
    print("Menu de operaciones\n")
    print("1.Calcular Area triangulo")
    print("2.Calcular Area rectangulo")
    print("3.Calcular Area rombo")
    print("4.Calcular Area circulo\n")
    opc=int(input("Ingrese opcion: "))
    if opc==1:
        base=float(input("Ingrese Base del triangulo: "))
        altura=float(input("Ingrese altura del triangulo: "))
        areaT=area_triangulo(base,altura)
        print("El area del triangulo es",areaT)
    elif opc==2:
        base=float(input("Ingrese Base del rectangulo: "))
        altura=float(input("Ingrese Altura del rectangulo: "))
        areaR=area_rectangulo(base,altura)
        print("El area del rectangulo es",areaR)
    elif opc==3:
        diagonal1=float(input("Ingrese diagonal mayor: "))
        diagonal2=float(input("Ingrese diagonal menor: "))
        areaRB=area_rombo(diagonal1,diagonal2)
        print("El area del rombo es",areaRB)
    elif opc==4:
        radio=float(input("Ingrese radio del circulo: "))
        areaRAD=area_circulo(radio)
        print("El area del circulo es",round(areaRAD,1))