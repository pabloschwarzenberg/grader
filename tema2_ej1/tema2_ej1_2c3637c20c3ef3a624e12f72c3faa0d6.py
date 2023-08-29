#Soy Oscar Páez
import math
def area_triangulo(base, altura):
    area = base * altura / 2
    return area
    


def area_rectangulo(base, altura):
    area = base * altura
    return(area)



def area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return(area)
    


def area_circulo(radio):
    area = math.pi * radio ** 2
    return(area)
    

print("Ingrese 1 si quiere el area de un triangulo")
print("Ingrese 2 si quiere el area de un rectangulo")
print("Ingrese 3 si quiere el area de un rombo")
print("Ingrese 4 si quiere el area de un circulo")
if __name__ == "__main__":
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        if __name__ == "__main__":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            area_triangulo(base, altura)
    elif opcion == 2:
        if __name__ == "__main__":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            area_rectangulo(base, altura)
    elif opcion == 3:
        if __name__ == "__main__":
            diagonal1 = float(input("Ingrese la diagonal 1: "))
            diagonal2 = float(input("Ingrese la diagonal 2: "))
            area_rombo(diagonal1, diagonal2)
    elif opcion == 4:
        if __name__ == "__main__":
            radio = float(input("ingrese el radio: "))
            area_circulo(radio)



    

           