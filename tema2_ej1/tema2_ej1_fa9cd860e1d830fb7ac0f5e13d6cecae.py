import math

def area_circulo(radio):
    area = math.pi*radio**2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_triangulo(base,altura):
    area = base*altura/2
    return area

def procesaOpciones(opcion):
    if opcion == 1:
        radio = float(input("\n          Ingresa radio: "))
        area = area_circulo(radio)
    elif opcion == 2:
        largo = float(input("\n          Ingresa largo: "))
        ancho = float(input("          Ingresa ancho: "))
        area = area_rectangulo(base,altura)
    elif opcion == 3:
        diagonal1 = float(input("\n          Ingresa diagonal1: "))
        diagonal2 = float(input("\n          Ingresa diagonal2: "))
        area = area_rombo(diagonal1,diagonal2)
    elif opcion == 4:
        base = float(input("\n          Ingresa base: "))
        altura = float(input("          Ingresa altura: "))
        area = area_triangulo(base,altura)
    return print("          El área es:", area)
        
def Menu():
    if __name__ == "__main__":
        opcion = 1
        while 1 <= opcion <= 5:
            print("\n                MENU")
            print("")
            print("          1. ÁREA CÍRCULO")
            print("          2. ÁREA RECTÁNGULO")
            print("          3. ÁREA ROMBO")
            print("          4. ÁREA TRIÁNGULO")
            print("          5. SALIR")
            print("")
            opcion = int(input("          Ingresa una opción: "))
            procesaOpciones(opcion)
     
Menu()