import math
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area

def area_circulo(radio):
    area = math.pi*(radio**2)
    return area

if __name__ == "__main__":
    g = input("Ingrese la figua a la cual le desea calcular el area")
    if g == "triangulo":
      b = float(input("Ingrese base"))
      h = float(input("Ingrese altura"))
      print(area_triangulo(a,h))
    elif g =="rectangulo":
      l1 = float(input("Ingrese lado1"))
      l2 = float(input("ingrese lado2"))
      print(area_rectangulo(l1,l2))
    elif g == "rombo":
      d1 = float(input("ingrese diagonal"))
      d2 = float(input("ingrese diagonal2"))
      print(area_rombo(d1,d2))
    elif g == "circulo":
      r = float(input("ingrese radio"))
      print(area_circulo(r))
      
           