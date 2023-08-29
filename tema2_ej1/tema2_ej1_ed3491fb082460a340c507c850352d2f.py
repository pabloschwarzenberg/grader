import math
def area_triangulo(base,altura):
    r = base*altura/2
    print("El area del triangulo de base ",base," y altura ",altura,"deberia ser ",r)
    pass

def area_rectangulo(largo,ancho):
    r = largo*ancho
    print("El area del rectangulo de lados ",largo," y ",ancho,"deberia ser ",r)
    pass

def area_rombo(diagonal1,diagonal2):
    r = diagonal1 * diagonal2 / 2
    print("El area del rombo con diagonales ",diagonal1,"y",diagonal2,"deberia ser",r)
    pass

def area_circulo(radio):
    r = math.pi * radio**2
    print("El area del circulo de radio ",radio,"debiera ser ",r)
    pass


if __name__ == "__main__":
    print("***************************************")
    print("Ingrese su eleccion")
    print("[ 1 ] area triangulo")
    print("[ 2 ] area rectangulo")
    print("[ 3 ] area rombo")
    print("[ 4 ] area circulo")
    eleccion = str(input("Su eleccion es "))
    if eleccion == "triangulo":
        base = int(input("Introduzca el valor de la base del triangulo"))
        altura = int(input("Introduzca el valor de la altura del triangulo"))
        area_triangulo(base,altura)
    if eleccion == "rectangulo":
        largo = int(input("Introduzca el valor del largo del rectangulo"))
        ancho = int(input("Introduzca el valor del ancho del rectangulo"))
        area_rectangulo(largo,ancho)
    if eleccion == "rombo":
        diagonal1 = int(input("Introduzca el valor de una diagonal del rombo"))
        diagonal2 = int(input("Introduzca el valor de la otra diagonal del rombo"))
        area_rombo(diagonal1,diagonal2)
    if eleccion == "circulo":
        radio = int(input("Introduzca el valor del radio"))
        area_circulo(radio)

        

