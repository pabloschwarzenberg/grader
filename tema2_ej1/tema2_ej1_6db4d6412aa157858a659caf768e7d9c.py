import math
def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area=math.pi*radio**2 
    return area

if __name__ == "__main__":
  area_triangulo(int(input()),int(input()))
  area_rectangulo(int(input()),int(input()))
  area_rombo(int(input()),int(input()))  
  area_circulo(int(input()))

    