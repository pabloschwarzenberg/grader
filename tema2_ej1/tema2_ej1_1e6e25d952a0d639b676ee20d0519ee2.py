import math
def area_triangulo(base,altura):
    area = base*altura/2
    return area
    pass

def area_rectangulo(base,altura):
    area = base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area
    pass

def area_circulo(radio):
    area = (math.pi)*radio**2
    return area
    pass

if __name__ == "__main__":
    a = input("¿que quieres calcular?:")
    b = [1, 2, 3, 4]
    if a == 1:
      altura = float(input())
      base = float(input())
      c = area_triangulo(base, altura)
    elif a == 2:
      altura = float(input())
      base = float(input())
      c = area_triangulo(base, altura)
    elif a == 3:
      diagonal1 = float(input())
      diagonal2 = float(input())
      c = area_rombo(diagonal1, diagonal2)
    elif a == 4:
      radio = float(input())
      c = area_circulo(radio)  
    pass
           