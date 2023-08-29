def area_triangulo(base,altura):
    return base*altura/2
def area_rectangulo(base,altura):
    return base*altura
def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2
def area_circulo(radio):
    from math import pi
    return pi*(radio**2)
if __name__=="__main__":
    print("1.- calcular area de un triangulo")
    print("2.- calcular area de un rectangulo")
    print("3.- calcular area de un rombo")
    print("4.- calcular area de un circulo")
    op=input('Ingrese el calculo que desea realizar: ')
    if op=='1':
        base=float(input('Ingrese la medida de la base: '))
        altura=float(input('Ingrese la medida de la altura: '))
        print(area_triangulo(base,altura))
    elif op=='2':
        base=float(input('Ingrese la medida de la base: '))
        altura=float(input('Ingrese la medida de la altura: '))
        print(area_rectangulo(base,altura))
    elif op=='3':
        d1=float(input('Ingrese la primera diagonal: '))
        d2=float(input('Ingrese la segunda diagonal: '))
        print(area_rombo(d1,d2))
    elif op=='4':
        r=float(input('Ingrese la medida del radio: '))
        print(area_circulo(r))           