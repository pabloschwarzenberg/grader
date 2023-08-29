from math import pi

def area_triangulo(base,altura):
    AreaT = (base*altura)/2
    return AreaT
 
def area_rectangulo(base,altura):
    AreaR = base*altura
    return AreaR

def area_rombo(diagonal1,diagonal2):
    AreaR = (diagonal1*diagonal2)/2
    return AreaR

def area_circulo(radio):
    AreaC = pi*(radio**2)
    return AreaC

def menu():
    print("OPCIÓN 1 = ÁREA TRIANGULO")
    print("OPCIÓN 2 = ÁREA RECTANGULO")
    print("OPCIÓN 3 = ÁREA ROMBO")
    print("OPCIÓN 4 = ÁREA CIRCULO")
    y = input("Ingrese opción: ")
    return y
        
if __name__ == "__main__":
    opc = menu()
    if opc == 1:
        a = input("Ingrese base: ")
        b = input("Ingrese altura: ")
        print(area_triangulo(a,b))
    if opc == 2:
        a = input("Ingrese base: ")
        b = input("Ingrese altura: ")
        print(area_rectangulo(a,b))
    if opc == 3:
        a = input("Ingrese diagonal 1: ")
        b = input("Ingrese diagonal 2: ")
        print(area_rombo(a,b))
    if opc == 5:
        r = int(input("Ingrese Radio: "))
        print(area_circulo(r))
    