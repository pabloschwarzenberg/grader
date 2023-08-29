from math import pi

def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area= pi*radio**2
    return area

def procesaOpciones(opcion):
    if opcion==1:
        radio= float(input("Ingresa base: "))
        altura= float(input("Ingresa altura: "))
        area= area_triangulo(base, altura)
        
    elif opcion==2:
        largo= float(input("Ingresa base: "))
        ancho= float(input("Ingresa altura: "))
        area= area_rectangulo(largo, ancho)
    elif opcion==3:
        diagonal1= float(input("Ingresa diagonal 1: "))
        diagonal2= float(input("Ingresa diagonal 2: ")) 
        area= area_rombo(diagonal1,diagonal2)
    elif opcion==4:
        radio= float(input("Ingresa radio: "))
        area= area_circulo(radio)
    if opcion in [1, 2, 3, 4]:
        print("el area es: ", area)
    
def Menu():
    opcion=1
    while opcion!=5:
        print("     MENU")
        print("")
        print("1. AREA TIRANGULO")
        print("2. AREA RECTANGULO")
        print("3. AREA ROMBO")
        print("4. AREA CIRCULO")
        print("5. SALIR")
        print("")
        opcion=int(input("Ingresa una opcion: "))
        procesaOpciones(opcion)


           