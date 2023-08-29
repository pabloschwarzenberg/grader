import math  
def area_triangulo(base,altura):
    cuadrado=base*altura
    area=cuadrado/2
    return (area)
def area_rectangulo(base,altura):
    area=base*altura
    return (area)
def area_rombo(diagonal1, diagonal2):
    cuadrado=diagonal1*diagonal2
    area=cuadrado/2
    return (area)
def area_circulo(radio):
    circulo=radio**2
    area=(math.pi*circulo)
    return area

if __name__=="__main__":
    print("Opciones de area a calcular: triangulo, rectangulo, rombo, circulo")
    opcion=input("Ingrese que quiere calcular:")
    if opcion=="triangulo":
        b=int(input("ingrese base:"))
        a=int(input("ingrese altura:"))
        print (area_triangulo(b,a))
    if opcion=="rectangulo":
        b=int(input("ingrese base:"))
        a=int(input("ingrese altura:"))
        print (area_rectangulo(b,a))
    if opcion=="rombo":
        b=int(input("ingrese diagonal1:"))
        a=int(input("ingrese diagonal2:"))
        print (area_rombo(b,a))
    if opcion=="circulo":
        b=int(input("ingrese radio:"))
        print (area_circulo(b))
      