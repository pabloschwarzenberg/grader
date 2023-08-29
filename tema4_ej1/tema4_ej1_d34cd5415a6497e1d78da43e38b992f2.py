import math
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area
    pass
def area_rectangulo(base,altura):
    area = base*altura
    return area 
    pass
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
    pass

def area_circulo(radio):
    pi = math.pi
    area = (radio**2)*pi
    return area
    pass
if __name__ == "__main__":
    print("Calculadora de area")
    while True: 
        print("Ingrese la opcion que desea usar")
        print("1. Calcular area de un triangulo\n2. Calcular area de un rectangulo")
        print("3. Calcular area de un rombo\n4. Calcular area de un circulo")
        a = int(input(""))
        if a == 1:
            base = int(input("Base del triangulo: "))
            altura = int(input("Altura del triangulo: "))
            print(area_triangulo(base,altura))
            break
        elif a == 2:
            base = int(input("Base del rectangulo: "))
            altura = int(input("Altura del rectangulo: "))
            print(area_rectangulo(base,altura))
            break
        elif a == 3:
            diagonal1 = int(input("Largo de la diagonal 1: "))
            diagonal2 = int(input("Largo de la diagonal 2: "))
            print(area_rombo(diagonal1,diagonal2))
            break
        elif a==4:
            radio=int(input("Radio del circulo: "))
            print(area_circulo(radio))
            break
        else:
            print("Ingrese una opcion valida")
    pass