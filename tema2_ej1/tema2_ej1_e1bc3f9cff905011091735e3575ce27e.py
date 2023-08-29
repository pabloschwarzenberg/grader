from math import pi

def area_rectangulo(ancho, largo):
    area = ancho*largo
    return area

def area_triangulo(base, altura):
    area = (base*altura)/2
    return area

def area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor*diagonal_menor)/2
    return area

def area_circulo(radio):
    area = pi*(radio**2)
    return area

if __name__ == "__main__":
    salir = False
    while not salir:
        print("MENU\n")
        print("1) Calcular área de un rectangulo")
        print("2) Calcular área de un triangulo")
        print("3) Calcular área de un rombo")
        print("4) Calcular área de una circunferencia")
        print("5) Salir")
        opcion = input("\nElija un opcion: ")
        if opcion == "1" or opcion == "1)":
            ancho = int(input("\nAncho del rectangulo: "))
            largo = int(input("Largo del rectangulo: "))
            area = area_rectangulo(ancho, largo)
            print("\nEl area del rectangulo es:", area)

        if opcion == "2" or opcion == "2)":
            base = int(input("\nBase del triangulo: "))
            altura = int(input("Alto del triangulo: "))
            area = area_triangulo(base, altura)
            print("\nEl area del triangulo es:", area)

        if opcion == "3" or opcion == "3)":
            diagonal_mayor = int(input("\nDiagonal mayor del rombo: "))
            diagonal_menor = int(input("Diagonal menor del rombo: "))
            area = area_rombo(diagonal_mayor, diagonal_menor)
            print("\nEl area del rombo es:", area)

        if opcion == "4" or opcion == "4)":
            radio = int(input("\nRadio de la circunferencia: "))
            area = area_circulo(radio)
            print("\nEl area de la circunferencia es:", area)

        if opcion == "5" or opcion == "5)":
            print("\nSaliendo...")
            salir = True

        print()
