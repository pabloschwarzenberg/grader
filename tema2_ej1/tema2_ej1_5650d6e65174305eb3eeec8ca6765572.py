from math import pi 
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rombo(diagonal,diagonal2):
    area=diagonal*diagonal2/2
    return area
def area_rectangulo(largo,ancho):
    area=largo*ancho
    return area
def area_circulo(radio):
    area=pi*radio**2
    return area
def procesaOpciones(opcion):
    if opcion==1:
        radio=float(input('Ingresa radio: '))
        area=areaCirculo(radio)
    elif opcion==2:
        largo=float(input('Ingresa el largo: '))
        ancho=float(input('Ingresa el ancho: '))
        area=areaRectangulo(largo,ancho)
    elif opcion==3:
        diagonal=float(input('Ingrese la diagonal 1: '))
        diagonal2=float(input('Ingrese la diagonal 2: '))
        area=areaRombo(diagonal,diagonal2)
    elif opcion==4:
        base=float(input('Ingrese la base: '))
        altura=float(input('Ingrese la altura: '))
        area=areaTriangulo(base,altura)
    if opcion in [1,2,3,4]:
        print('El área es:',area)
