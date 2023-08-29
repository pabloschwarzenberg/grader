from math import pi
def area_triangulo(altura,base):
    area = (altura * base)/2
    return area

def area_rombo(dP,dS):
    area = (dP*dS)/2
    return area

def area_rectangulo(ancho,largo):
    area = ancho * largo
    return area

def area_circulo(radio):
    area = pi *(radio**2)
    return area

def procesaOpciones(opcion): 
    if opcion == 1:
        radio = float(input("ingresa radio: " ))
        area = area_circulo(radio)
        print("El área es:", area)
    elif opcion == 2:
        ancho = float(input("ingresa ancho: " ))
        largo = float(input("ingresa largo: " ))
        area = area_rectangulo(ancho,largo)
        print("El área es:", area)
    elif opcion == 3:
        dP = float(input("ingresa un lado: " ))
        dS = float(input("ingresa un lado: " ))
        area = area_rombo(dP,dS)
        print("El área es:", area)
    elif opcion == 4:
        altura = float(input("ingresa la altura: " ))
        base = float(input("ingresa la base: " ))
        area = area_triangulo(altura,base)
        print("El área es:", area)

def Menu():
    opcion = 0
    while opcion != 5:
        print("\n                MENU")
        print("")
        print("          1. ÁREA CÍRCULO")
        print("          2. ÁREA Rectangulo")
        print("          3. ÁREA Rombo")
        print("          4. ÁREA TRIÁNGULO")
        print("          5. SALIR")
        print("")
        opcion = int(input("ingresa una opción: "))
        procesaOpciones(opcion)