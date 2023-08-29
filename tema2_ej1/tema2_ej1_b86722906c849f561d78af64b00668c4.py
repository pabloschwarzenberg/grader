from math import pi 

def area_triangulo(base,altura):
    area = base*altura/2
    return area
def area_rectangulo(base,altura):
    area = base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area 
def area_circulo(radio):
    area = pi*radio*radio
    return area

    


print("""Qué desea calcular?"
0: Calcular el área de un triángulo
1: Calcular el área de un rectángulo
2: Calcular el área de un rombo
3: Calcular el área de un círculo
""")

if __name__ == "__main__":
    
    figura = int(input("(0,1,2,3): "))

    if figura == 0:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        print(area_triangulo(base,altura))
    elif figura == 1:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        print(area_triangulo(base,altura))
    elif figura == 2:
        diagonal1 = float(input("Ingrese una diagonal: "))
        diagonal2 = float(input("Ingrese la otra diagonal: "))
        print(area_rombo(diagonal1,diagonal2))
    elif figura == 3:
        radio = float(input("Ingrese el radio: "))
        print(area_circulo(radio))