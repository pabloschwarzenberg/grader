def area_triangulo(base,altura):
    a = float(base * altura)/2
    return a

def area_rectangulo(base,altura):
    a = float(base * altura)
    return a

def area_rombo(diagonal1,diagonal2):
    a = float((diagonal1 * diagonal2)/2)
    return a

def area_circulo(radio):
    a = float(3.14159265358979323846 * (radio ** 2))
    return a

if __name__ == "__main__":
  b = input("Elige tipo de figura: ")
  if b == ("triangulo"):
      altura = float(input("Ingresa altura: "))
      base = float(input("Ingresa base: "))
      print(area_triangulo(base,altura))
  elif b == ("rectangulo"):
      altura = float(input("Ingrese altura: "))
      base = float(input("Ingrese base: "))
      print(area_rectangulo(base,altura))
  elif b == ("rombo"):
      diagonal1 = float(input("Ingrese primera diagonal: "))
      diagonal2 = float(input("Ingrese segunda diagonal: "))
      print(area_rombo(diagonal1,diagonal2))
  elif b == ("circulo"):
      radio = float(input("Ingrese radio: "))
      print(area_circulo(radio))          