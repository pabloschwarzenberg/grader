import math
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area
#("el area del triangulo es " + str(area) + " unidades cuadradas") 

def area_rectangulo(base,altura):
    area = base*altura
    return area
#("el area del rectangulo es " + str(area) + " unidades cuadradas") 

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
#("el area del rombo es " + str(area) + " unidades cuadradas") 

def area_circulo(radio):
    area = math.pi*(radio**2)
    return area
#print(("el area del circulo es " + str(area) + " unidades cuadradas"))
if __name__ == "__main__":
    loop = 1
    while loop == 1:
        print("BIENVENIDO A LA CALCULADORA DE AREAS")
        print(" ")
        print("tus opciones son: ")
        print("1) triangulo")
        print("2) rectangulo (cuadrado)")
        print("3) rombo")
        print("4) circulo")
        print("5) salir del programa")
        print(" ")
        areap = int(input("¿a que figura geometrica le desea calcular el area?: "))
        if areap == 1:
            base = int(input("¿su triangulo posee una base de cuantas unidades?: "))
            altura = int(input("¿su triangulo posee una altura de cuantas unidades?: "))
            area_triangulo(base,altura)
        elif areap == 2:
            base = int(input("¿su rectangulo posee una base de cuantas unidades?: "))
            altura = int(input("¿su rectangulo posee una altura de cuantas unidades?: "))
            area_rectangulo(base,altura)
        elif areap == 3:
            base = int(input("¿su rombo posee una diagonal1 de cuantas unidades?: "))
            altura = int(input("¿su rombo posee una diagonal2 de cuantas unidades?: "))
            area_rombo(base,altura)
        elif areap == 4:
            radio = int(input("¿su circulo posee un radio de cuantas unidades?: "))
            area_circulo(radio)
        elif areap == 5:
            loop = 0 
        else:
            print("input no valido, porfavor elija una opcion del 1 al 5")
            loop = 1

