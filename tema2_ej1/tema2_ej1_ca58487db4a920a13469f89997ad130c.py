from math import pi
def area_triangulo(base,altura):
    return(base*altura/2)

def area_rectangulo(base,altura):
    return(base*altura)

def area_rombo(diagonal1,diagonal2):
    return(diagonal2*diagonal1/2)

def area_circulo(radio):
    return (pi*radio**2)

if __name__ == "__main__":
  area_triangulo(input(float("ingrese un numero:")),input(float("ingrese un numero:")))
  area_rectangulo(input(float("ingrese el ancho:")),input(float("ingrese el largo:")))
  area_rombo(input(float("ingrese diagonal1: ")),input(float("ingrese diagonal2: ")))
  area_circulo(input(float("ingrese el radio:")))  