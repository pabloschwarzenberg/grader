from math import pi

def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    return radio*radio*pi

if __name__ == "__main__":
    print("--menu--")
    print("1. área triángulo")
    print("2. área rectángulo")
    print("3. área rombo")
    print("4. área círculo")
    x = int(input("ingrese opción: "))
    
    if x == 1:
      base = input("ingrese base: ")
      altura = input("ingrese altura: ")
      print(area_triangulo(base, altura))
    elif x == 2:
      base = input("ingrese base: ")
      altura = input("ingrese altura: ")
      print(area_rectangulo(base, altura))
    elif x == 3:
      diagonal1 = input("ingrese diagonal1: ")
      diagonal2 = input("ingrese diagonal2: ")
      print(area_rombo(diagonal1, diagonal2))
    elif x == 4:
      radio = input("ingrese radio: ")
      print(area_circulo(radio))
      
           