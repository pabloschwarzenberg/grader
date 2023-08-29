from math import pi
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
    pi*(r**2)
    return area
    pass

print("""1 : Triángulo
2 : Rectángulo
3 : Rombo
4 : Cículo""")

figura = float(input("Ingrese tipo de figura: "))
while figura != 1 and figura != 2 and figura != 3 and figura != 4:
    print("Valor invalido, por favor refloatente")
    figura = float(input("Ingrese tipo de figura: "))

if figura == 1:
    print("")
    print("Triángulo")
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = area_triangulo(base,altura)
    print(area)
    
if figura == 2:
    print("")
    print("Rectángulo")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = area_rectangulo(base,altura)
    print(area)
    
if figura == 3:
    priny("")
    print("Rombo")
    diagonal1 = float(input("Ingrese una digonal del rombo: "))
    diagonal2 = float(input("Ingrese la otra diagonal del rombo: "))
    area = area_rombo(diagonal1,diagonal2)
    print(area)

if figura == 4:
    print("Cículo")
    print("")
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print(area)