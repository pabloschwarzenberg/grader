def area_triangulo(base,altura):
    aT=(base*altura)/2
    return aT

def area_rectangulo(base,altura):
    aR=base*altura
    return aR

def area_rombo(diagonal1,diagonal2):
    aRo=(diagonal1*diagonal2)/2
    return aRo

def area_circulo(radio):
    aC=3.141592653589793125*(radio**2)
    return aC

#Muestra Menu
menu=["1. Area Triangulo",
      "2. Area Rectangulo",
      "3. Area Rombo",
      "4. Area Circulo"]
for linea in menu:
    print(linea)
#Llama Funciones
def menu(op):
    if op==1:
        b=int(input("Ingrese base: "))
        h=int(input("Ingrese altura: "))
        area_triangulo(b,h)
    if op==2:
        b=int(input("Ingrese base: "))
        h=int(input("Ingrese altura: "))
        area_rectangulo(b,h)
    if op==3:
        d1=int(input("Ingrese diagonal 1: "))
        d2=int(input("Ingrese diagonal 2: "))
        area_rombo(d1,d2)
    if op==4:
        r=int(input("Ingrese radio: "))
        area_circulo(r)
