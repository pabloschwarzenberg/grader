import math

def area_triangulo(base,altura):
    areatriangulo=((base*altura)/2)
    return areatriangulo

def area_rectangulo(base,altura):
    arearectangulo=(base*altura)
    return arearectangulo

def area_rombo(diagonal1,diagonal2):
    arearombo=((diagonal1*diagonal2)/2)
    return arearombo

def area_circulo(radio):
    areacirculo=((radio**2)*math.pi)
    return areacirculo

if __name__ == "__main__":
    print("*** Bienvenido a la calculador geometrica ***")

    while True:
        print("¿Que figura desea calcular el area?")
        print("1: Triangulo")
        print("2: Rectangulo")
        print("3: Rombo")
        print("4: Circulo")
        n=int(input("Coloque el numero de la figura que desea calcular: "))

        if n==1:
            base1=float(input("Ingrese la base: "))
            altura1=float(input("Ingrese la altura: "))
            print("El area del triangulo es: ",area_triangulo(base1,altura1))
            break

        elif n==2:
            base2=float(input("Ingrese un lado: "))
            altura2=float(input("Ingrese el otro lado: "))
            print("El area del rectangulo es: ",area_rectangulo(base2,altura2))
            break

        elif n==3:
            diagonal13=float(input("Ingrese la diagonal larga: "))
            diagonal23=float(input("Ingrese la diagonal corta: "))
            print("El area del rombo es: ",area_rombo(diagonal13,diagonal23))
            break

        elif n==4:
            radio4=float(input("Ingrese el radio: "))
            print("El area del circulo es: ",area_circulo(radio4))
            break

        else:
            print("No existe esa opcion, intente de nuevo")