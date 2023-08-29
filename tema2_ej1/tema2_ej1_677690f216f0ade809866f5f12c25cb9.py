import math
def area_triangulo(base,altura):
    areaTriangulo=base*altura/2
    return areaTriangulo

def area_rectangulo(base,altura):
    areaRectangulo=base*altura
    return areaRectangulo

def area_rombo(diagonal1,diagonal2):
    areaRombo=(diagonal1*diagonal2)/2
    return areaRombo

def menu():
    print("Ingrese una opcion")
    print("[1]Area Triangulo\n[2]Area Rectangulo\n[3]Area Rombo\n[4]Area Circulo\n[5]SALIR")
def area_circulo(radio):
    areaCirculo=(math.pi*radio**2)
    return areaCirculo

if __name__ == "__main__":
    while (True):
        menu()
        search=int(input("--> "))
        if search==1:
            print("Ha ingresado area triangulo")
            baset=int(input("Ingrese valor de base del triangulo: "))
            alturat=int(input("Ingrese valor de altura del triangulo: "))
            print("El area del triangulo es de: ",area_triangulo(baset,alturat))
        if search==2:
            print("Ha ingresado area rectangulo")
            baser=int(input("Ingrese valor de base del rectangulo: "))
            alturar=int(input("Ingrese valor de altura del rectangulo: "))
            print("El area del rectangulo es de: ",area_rectangulo(baser,alturar))
        if search==3:
            print("Ha ingresado Area Rombo")
            diagonal11=int(input("Ingrese diagonal 1: "))
            diagonal22=int(input("Ingrese diagonal 2: "))
            print("El area del rombo es de: ",area_rombo(diagonal11,diagonal22))
        if search==4:
            print("Ha ingresado Area Circulo")
            radioo=int(input("Ingrese radio del circulo: "))
            print("El area del circulo es de: ", area_circulo(radioo))
        if search==5:
            print("Saliendo...")
            break
