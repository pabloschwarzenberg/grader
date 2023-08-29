import math
def area_triangulo(base,altura):
    return((base*altura)/2)

def area_rectangulo(base,altura):
    return(base*altura)

def area_rombo(diagonal1,diagonal2):
    return((diagonal1 * diagonal2)/2)

def area_circulo(radio):
    return(math.pi*(radio**2))

def main():
    print("Menu \n 1. Area Triangulo \n 2. Area Rectangulo \n 3. Area Rombo \n 4. Area Circulo ")
    n = int(input("ingrese opcion: "))
    if n == 1:
        base = int(input("ingrese base: "))
        altura = int(input("ingrese altura: "))
        print(area_triangulo(base, altura))
    elif n == 2:
        base = int(input("ingrese base: "))
        altura = int(input("ingrese altura: "))
        print(area_rectangulo(base, altura))
    elif n ==3:
        diagonal1 = int(input("ingrese diagonal 1: "))
        diagonal2 = int(input("ingrese diagonal 2: "))
        print(area_rombo(diagonal1, diagonal2))
    elif n == 4:
        radio = int(input("ingrese radio: "))
        print(area_circulo(radio))
    
if __name__ == "__main__":
    main()
           
