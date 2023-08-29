import math
base=0
altura=0
largo=0
ancho=0
diagonal1=0
diagonal2=0
radio=0

def area_triangulo(base,altura):
    area = base * altura / 2
    return area

def area_rectangulo(largo,ancho):
    area = largo * ancho
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/ 2
    return area

def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

if __name__ == "__main__":

    print("Calcular Áreas de figuras Geométricas.\n")
    print("1.Rectangulo.\n2.Trinagulo.\n3.Rombo.\n4.Circulo.\n")

    menu = int(input("Escoja la figura: "))

    if menu == 1:
        largo = float(input('Ingrese la Largo: '))
        ancho = float(input('Ingrese la Ancho: '))
        area_rectangulo(largo, ancho)

    if menu == 2:
          base = float(input('Ingrese la base: '))
          altura = float(input('Ingrese la altura: '))
          area_triangulo(base, altura)

    if menu == 3:
        diagonal1 = float(input('Ingrese la diagonal mayor: '))
        diagonal2 = float(input('Ingrese la diagonal menor: '))
        area_rombo(diagonal1,diagonal2)

    if menu == 4:
        radio = float(input('Ingrese el radio:'))
        area_circulo(radio)
