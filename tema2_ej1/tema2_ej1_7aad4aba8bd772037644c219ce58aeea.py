import math
PI = math.pi



def area_triangulo(base,altura):
    AreaT = ((base*altura)/2)
    return AreaT

def area_rectangulo(base,altura):
    AreaR = (base*altura)
    return AreaR
    

def area_rombo(diagonal1,diagonal2):
    AreaRombo = (diagonal1*diagonal2)/2
    return AreaRombo
    

def area_circulo(radio):
    AreaCirculo = (PI*((radio)**2))
    return AreaCirculo
    

if __name__ == "__main__":
    pass

menu = 0


print("\n1.- Area de un triangulo")
print("2.- Area de un rectangulo")
print("3.- Area de un rombo")
print("4.- Area de un ciruculo")
print("para salir del programa ingrese cualquier otro numero")
if __name__ == "__main__":

    Opcion = int(input("\nIngrese su opcion >>> "))
    if Opcion == 1:
        BaseT = int(input("\nIngrese la base del triangulo >>> "))
        AlturaT = int(input("\nIngrese la altura del triangulo >>> "))
        area_triangulo(BaseT,AlturaT)
    elif Opcion == 2:
        BaseR = int(input("\nIngrese la base del rectangulo >>> "))
        AlturaR = int(input("\nIngrese la altura del rectangulo >>> "))
        area_rectangulo(BaseR,AlturaR)
    elif Opcion == 3:
        Diagonal1 = int(input("\nIngrese la primera diagonal >>> "))
        Diagonal2 = int(input("\nIngrese la segunda diagonal >>> "))
        area_rombo(Diagonal1,Diagonal2)
    elif Opcion == 4:
        Radio = int(input("\nIngrese el radio del circulo >>> "))
        area_circulo(Radio)
    else:
        menu += 5
        print("Adios")
