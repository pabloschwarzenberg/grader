Pi=3.1415
def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area


def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2
    return area

def area_circulo(radio):
    global Pi
    area= Pi*radio**2
    return area
print("0_triangulo")
print("1_rectangulo")
print("2_rombo")
print("3_circulo")
nombre=int(input("ingrese que area desea calcular:"))


if nombre == 0:
    base = int(input("ingrese la base del triangulo:"))
    altura = int(input("ingrese la altura del triangulo:"))
    print("el area del triangulo es:", area_triangulo(base,altura))
elif nombre ==1:
    base = int(input("ingrese la base del rectangulo:"))
    altura = int(input("ingrese la altura del rectangulo:"))
    print("el area del rectangulo es:",area_rectangulo(base,altura))
elif nombre==2:
    diagonal1 = int(input("ingrese la diagonal1 del rombo:"))
    diagonal2 = int(input("ingrese la diagonal2 del rombo:"))
    print("el area del rombo es:", area_rombo(diagonal1,diagonal2))
elif nombre==3:
    radio = int(input("ingrese el radio del circulo:"))
    print("el area del circulo es:",area_circulo(radio))

 
           