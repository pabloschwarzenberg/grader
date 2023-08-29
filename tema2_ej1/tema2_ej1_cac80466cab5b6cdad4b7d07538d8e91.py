import math
decision=int(input("Que desea calcular: (1)area de un triangulo (2)area de un rectangulo"
               " (3)area de un rombo (4)area de un circulo"))
def area_triangulo(base,altura):
    x=round((base*altura)/2,1)
    return 'El area del triangulo es ',x
def area_rectangulo(base,altura):
    x=round(base*altura,1)
    return "El area del rectangulo es ",x
def area_rombo(diagonal1,diagonal2):
    x=round((diagonal1*diagonal2)/2,1)
    return "El area del rombo es ",x
def area_circulo(radio):
    x=round(math.pi*(radio**2),1)
    return "El area del circulo es ",x
if decision==1:
    b=int(input("El valor de la base: "))
    a = int(input("El valor de la altura: "))
    print(area_triangulo(b,a))
if decision==2:
    b = int(input("El valor de la base: "))
    a = int(input("El valor de la altura: "))
    print(area_rectangulo(b, a))
if decision==3:
    d1 = int(input("El valor de la base: "))
    d2 = int(input("El valor de la altura: "))
    print(area_rombo(d1, d2))
if decision==4:
    r=int(input("El valor del radio: "))
    print(area_circulo(r))