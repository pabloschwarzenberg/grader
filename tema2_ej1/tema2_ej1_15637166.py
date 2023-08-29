import math

def area_triangulo(base,altura):
    area=base*altura/2
    return area
        
def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area

if __name__ == "__main__":
    print("¿A que figura deseea calcular su area?")
    d=input("¿triangulo, rectangulo, rombo o circulo?:")
    if d=="triangulo":
        e=eval(input("Ingrese base:"))
        f=eval(input("Ingrese altura:"))
        g=area_triangulo(e,f)
        print("El area del triangulo es:",g)
    elif d=="rectangulo":
        e=eval(input("Ingrese base:"))
        f=eval(input("Ingrese altura:"))
        g=area_rectangulo(e,f)
        print("El area del rectangulo es:",g)
    elif d=="rombo":
        e=eval(input("Ingrese diagonal 1:"))
        f=eval(input("Ingrese diagonal 2:"))
        g=area_rombo(e,f)
        print("El area del rombo es:",g)
    elif d=="circulo":
        e=eval(input("Ingrese radio del circulo:"))
        g=area_circulo(e)
        print("El area del circulo es:",g)
        
           