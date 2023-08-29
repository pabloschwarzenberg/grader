import math
def area_triangulo(base,altura):
    resultado=(base*altura)/2
    return resultado
def area_rectangulo(base,altura):
    resultado= base*altura
    return resultado
def area_rombo(diagonal1,diagonal2):
    resultado= (diagonal1*diagonal2)/2
    return resultado
def area_circulo(radio):
    resultado= math.pi*(radio**2)
    return resultado
if __name__ == "__main__":
    def menu():
        print('''      Esto es una calculadora Geométrica
        Qué operacion desea realizar?
                 1-Calcular el área de un triángulo
                 2-Calcular el área de un rectángulo
                 3-Calcular el área de un rombo
                 4-Calcular el área de un circulo''')
        elige = int(input("         Elige una de las opciones: "))
        return (elige)
    opcion=menu()
    if opcion == 1 or opcion == 2:
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
    if opcion == 1:
        print(area_triangulo(base, altura))
    if opcion == 2:
        print(area_rectangulo(base, altura))
    if opcion == 3:
        diagonal1 = int(input("Ingrese el valor de la primera diagonal "))
        diagonal2 = int(input("Ingrese el valor de la segunda diagonal: "))
        print(area_rombo(diagonal1, diagonal2))
    if opcion == 4:
        radio = int(input("Ingrese el valor de el radio: "))
        print(area_circulo(radio))