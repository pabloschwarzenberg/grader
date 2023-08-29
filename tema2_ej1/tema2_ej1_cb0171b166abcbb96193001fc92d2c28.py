from math import pi

def area_triangulo(base,altura):
    area = base*altura/2
    return area 

def area_rectangulo(largo,ancho):
    area = largo*ancho 
    return area 

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area 

def area_circulo(radio):
    area =  pi * (radio**2)
    return area

def procesaOpciones(opcion):

    if opcion == 1:
        altura = float(input("\n     ingresa altura del triangulo:"))
        base = float(input("\n     ingresa base del triangulo :"))
        area = area_triangulo(base,altura)
    elif opcion == 2:
        largo =float(input("\n     ingresa largo del rectangulo:"))
        ancho =float(input("\n     ingresa ancho del rectangulo:"))
        area = area_rectangulo(largo,ancho)
    elif opcion == 3:
        diagonal1 =float(input("\n     ingresa la diagonal1 del Rombo:"))
        diagonal2 =float(input("\n     ingresa la diagonal2 del Rombo :"))
        area = area_rombo(diagonal1,diagonal2)
    elif opcion == 4:
        radio = float(input("\n     ingresa radio:"))
        area = area_circulo(radio)
    if opcion in [1,2,3,4]:
         print("El area es:", area)
def Menu():
    opcion = 0
    while opcion != 5:
        print("\n                MENU")
        print("")
        print("          1. ÁREA TRIÁNGULO")
        print("          2. ÁREA RECTÁNGULO")
        print("          3. ÁREA ROMBO")
        print("          4. ÁREA CIRCULO")
        print("")
        opcion = int(input("          Ingresa una opción: "))
        procesaOpciones(opcion)

if __name__ == "__main__":
 Menu()   