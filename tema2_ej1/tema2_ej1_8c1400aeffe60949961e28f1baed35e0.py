from math import pi

def area_triangulo(base,altura):
    n=(base*altura)/2
    return n

def area_rectangulo(base,altura):
    n=base*altura
    return n

def area_rombo(diagonal1,diagonal2):
    n=(diagonal1*diagonal2)/2
    return n

def area_circulo(radio):
    global pi
    n=(radio**2)*pi
    return n


if __name__ == "__main__":
    print("escoja una opcion:")
    print("1: area de triangulo")
    print("2: area de rectangulo")
    print("3: area de rombo")
    print("4: area de circulo")
    a=int(input("Su opcion es: "))



    if a==1:
        basex=float(input("base del triangulo: "))
        alturax=float(input("altura del triangulo: "))
        resultado=area_triangulo(basex,alturax)
        print(resultado)

    if a==2:
        basex=float(input("base del rectangulo: "))
        alturax=float(input("altura del rectangulo: "))
        resultado=area_rectangulo(basex,alturax)
        print(resultado)

    if a==3:
        d1=float(input("diagonal 1 del rombo: "))
        d2=float(input("diagonal 2 del rombo: "))
        r=area_rombo(d1,d2)
        print(r)

    if a==4:
        radiox=float(input("radio del circulo: "))
        r=area_circulo(radiox)
        print(r)