from math import pi
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return pi*radio**2

if __name__ == "__main__":
   area_calcular=int(input("¿Que desea calcular?\1) Area triangulo\2)Area rectangulo\3) Area Rombo\4) Area circulo"))
           