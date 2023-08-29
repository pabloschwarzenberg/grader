import math

def menu():
    print("1-. Triangulo")
    print("2-. Rectangulo")
    print("3-. Rombo")
    print("4-. Circulo")
    figura=int(input("Figura a la cual le quieres calcular el area: "))

    if figura==1:
        area_triangulo()
    if figura==2:
        area_rectangulo()
    if figura==3:
        area_rombo()
    if figura==4:
        area_circulo()

def area_triangulo():
    basetri=int(input("Ingrese la base del triagunlo: "))
    alturatri=int(input("Ingrese la altura del triangulo: "))
    areatri = (basetri*alturatri)/2
    print("El area de su triangulo es de ",areatri,"unidades cuadradas.")

def area_rectangulo():
    baserect=int(input("Ingrese la base del rectangulo: "))
    alturarect=int(input("Ingrese la altura del rectangulo: "))
    arearect=(baserect*alturarect)
    print("El area de su rectangulo es de ",arearect,"unidades cuadradas.")

def area_rombo():
    diagonal1=int(input("Ingrese el valor de la diagonal principal: "))
    diagonal2=int(input("Ingrese el valor de la segunda diagonal: "))
    arearombo=(diagonal1*diagonal2)/2
    print("El area de su rombo es de ",arearombo," unidades cuadradas.")

def area_circulo():
    radio=int(input("Ingrese el radio de su circulo: "))
    areacirc=math.pi *(radio**2)
    print("El area de su circulo es de ",areacirc," unidades cuadradas")

menu()      