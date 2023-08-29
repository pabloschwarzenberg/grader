from math import pi
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = pi*(radio**2)
    return area

if __name__ == "__main__":
    opcion = input("Que area desea calcular, triangulo,rectangulo,rombo o circulo")
    if opcion == "triangulo":
       base = int(input("Ingrese base:"))
       altura = int(input("Ingrese altura:"))
       print(area_triangulo(base,altura))
    elif opcion == "rectangulo":
         base = int(input("Ingrese base:"))
         altura = int(input("Ingrese altura:"))
         print(area_rectangulo(base,altura))
    elif opcion == "rombo":
         diagonal1 = int(input("Ingrese diagonal1:"))
         diagonal2 = int(input("Ingrese siagonal2:"))
         print(area_rombo(diagonal1,diagonal2))
    elif opcion == "circulo":
         radio = int(input("Ingrese el radio:"))
         print(area_circulo(radio))
    else:
         print("Figura invalida")
           