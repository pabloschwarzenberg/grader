import math
def area_triangulo(base, altura):
    return base * altura /2
    
    pass

def area_rectangulo(base, altura):
    return base * altura

    
    pass

def area_rombo(diagonal1, diagonal2):

    return diagonal1 * diagonal2 /2
    
    pass

def area_circulo(radio):

    return math.pi *radio **2
    
    pass
if __name__== "__main__":
    base=int(input("Ingrese la base del tringulo: "))
    altura=int(input("Ingrese la altura del tringulo: "))
    print("El area del tringulo es: ")
    base=int(input("Ingrese la base del rectangulo: "))
    altura=int(input("Ingrese la altura del rectangulo: "))
    print("El area del ractangulo es: ")
    diagonal1=int(input("Ingrese la diagonal1: "))
    diagonal2=int(input("Ingrese la diagonal2: "))
    print("El area del rombo es: ")
    radio=int(input("Ingrese el radio del circulo: "))
    print("El area del circulo es: ")


    pass