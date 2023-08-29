import math
def area_triangulo(base,altura):
    area1=int(base)*int(altura)/2
    return area1

def area_rectangulo(base,altura):
    area2=int(base)*int(altura)
    return area2

def area_rombo(diagonal1,diagonal2):
    area3=int(diagonal1)*int(diagonal2)/2
    return area3

def area_circulo(radio):
    area=math.pi*(int(radio))**2
    return area
opcion = 0
if __name__ == "__main__":
  while opcion != -1:
    print("(1) Área de un triángulo \n(2) Área de un rectángulo \n(3) Área de un rombo \n(4) Área de un círculo \n(-1) Salir del menú")
    opcion = int(input("Que desea hacer? "))
    if opcion == 1:
        base = input("Ingrese base del triángulo\n")
        altura = input("Ingrese altura del triángulo\n")
        area1 = area_triangulo(base,altura)
        print("el area es ", area1)
    if opcion == 2:
        base = input("Ingrese base del rectangulo\n")
        altura = input("Ingrese altura del rectangulo\n")
        area2 = area_rectangulo(base,altura)
        print(" el area es ", area2)
    if opcion==3:
        diagonal1 = input("Ingrese diagonal 1 del rombo\n")
        diagonal2 = input("Ingrese diagonal 2 del rombo\n")
        area3 = area_rombo(diagonal1,diagonal2)
        print("el area es ", area3)
    if opcion==4:
        radio = input("Ingrese radio del circulo\n")
        area = area_circulo(radio)
        print("el area es ", area)
    if opcion == -1:
        print("Nos vemos")
    else:
        print("Opcion incorrecta")