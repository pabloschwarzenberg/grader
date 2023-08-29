from math import pi

def area_triangulo(base,altura):
    area_de_triangulo = (base * altura)/2
    return area_de_triangulo
    

def area_rectangulo(base,altura):
    area_de_rectangulo = (base * altura)
    return area_de_rectangulo
    

def area_rombo(diagonal1,diagonal2):
    area_de_rombo = (diagonal1* diagonal2)/2
    return area_de_rombo
    

def area_circulo(radio):
    area_de_circulo = pi * radio**2
    return area_de_circulo

    

print("escoja alguna de las siguientes opciones: ")
print("1: area de triangulo")
print("2: area de rectangulo")
print("3: area de rombo")
print("4: area de circulo")
if __name__ == "__main__":
    opcion = int(input("escoja opcion: "))
    if opcion == 1:
        base = int(input("indique valor de la base por favor: "))
        altura = int(input("indique valor de la altura por favor: "))
        print("mi area triangulo es:",area_triangulo(base, altura))
    if opcion == 2:
        base = int(input("indique valor de la base por favor: "))
        altura = int(input("indique valor de la altura por favor: "))
        print("mi area rectangulo es:",area_rectangulo(base, altura))
    if opcion == 3:
        diagonal1 = int(input("indique el valor de diagonal 1: "))
        diagonal2 = int(input("indique valor de diagonal 2: "))
        print("mi area del rombo es:",area_rombo(diagonal1,diagonal2))
    if opcion == 4:
        radio = int(input("ingrese valor del radio: "))
        print("el area del circulo es:",area_circulo(radio))
    else:
        pass           