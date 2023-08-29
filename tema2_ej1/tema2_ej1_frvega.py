import math
def area_triangulo(base,altura):
    r = (base*altura)/2
    return r

def area_rectangulo(base,altura):
    s = base*altura
    return s
    

def area_rombo(diagonal1,diagonal2):
    t= (diagonal1*diagonal2)/2
    return t

def area_circulo(radio):
    u= math.pi*(radio)**2
    return u

if __name__ == "__main__":
    print("1: Area Triangulo")
    print("2: Area Rectangulo")
    print("3: Area Rombo")
    print("4: Area Circulo")
    opcion=int(input("Que desea Calcular?: "))
    if opcion == 1:
        a=int(input("Ingrese base: "))
        b=int(input("Ingrese altura: "))
        print("Su area es:", area_triangulo(a,b))
    elif opcion ==2:
        a=int(input("Ingrese base: "))
        b=int(input("Ingrese altura: "))
        print("Su area es:", area_rectangulo(a,b))
    elif opcion ==3:
        a=int(input("Ingrese diagonal 1: "))
        b=int(input("Ingrese diagonal 2: "))
        print("Su area es:", area_rombo(a,b))
    elif opcion ==4:
        a=int(input("Ingrese radio: "))
        print("Su area es:", area_circulo(a))
           
