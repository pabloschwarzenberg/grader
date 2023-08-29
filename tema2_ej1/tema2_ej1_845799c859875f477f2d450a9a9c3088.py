from math import pi


def area_triangulo(base,altura):
    a_t = (base*altura)/2
    return(a_t)
    
def area_rectangulo(base,altura):
    a_r = base*altura
    return(a_r)
    
def area_rombo(diagonal1,diagonal2):
    a_rom = (diagonal1*diagonal2)/2
    return(a_rom)

def area_circulo(radio):
    a_c = pi * (radio**2)
    return(a_c)

def menu():
    print("""
1 - Area Triangulo
2 - Area Rectangulo
3 - Area Rombo
4 - Area Circulo
""")
    __name__ = int(input("Que desea hacer: "))
    if __name__ == 1:
        b = int(input("ingresa base: "))
        a = int(input("ingresa altura: "))
        area_triangulo(b,a)
    if __name__ == 2:
        b = int(input("ingresa base: "))
        a = int(input("ingresa altura: "))
        area_rectangulo(b,a)
    if __name__ == 3:
        b = int(input("ingresa diagonal 1: "))
        a = int(input("ingresa diagonal 2: "))
        area_rombo(b,a)
    if __name__ == 4:
        r = int(input("ingresa radio: "))
        area_circulo(r)
    
menu()