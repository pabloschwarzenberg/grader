import math
def area_triangulo(base, altura):
    S = (base * altura)/ 2
    return S
def area_circulo(radio):
    S = math.pi * (radio**2)
    return S
def area_rombo(diagonal1,diagonal2):
    S = (diagonal1*diagonal2)/2
    return S
def area_rectangulo(base,altura):
    S = base * altura
    return S

if __name__ == "__main__":
  calcular=int(input("Ingrese la figura geometrica a la que desea calcular superficie,(1)triangulo,(2) circulo, (3) rombo, (4) rectangulo: "))
  if calcular == 1:
    base = float(input("ingrese medida de la base del tringulo: "))
    altura = float(input("ingrese medida de la altura del triangulo: "))
    print("La superficie del triangulo es: ",area_triangulo(base,altura))
  elif calcular == 2:
    radio = float(input("ingrese medida del radio del circulo: "))
    print("el area de la circunferencia es: ", area_circulo(radio))
  elif calcular == 3:
    D1 = float(input("Ingrese diagonal mayor del rombo: "))
    D2 = float(input("ingrese diagonal menor del rombo: "))
    print("la superficie del rombo es: ",area_rombo(D1,D2))
  elif calcular == 4:
    B =float(input("Ingrese el ancho del rectangulo: "))
    H = float(input("ingrese el largo del rectangulo: "))
    print("la superficie del rectangulo es: ", area_rectangulo(B,H))
  else:
    print("no ha ingresado ninguna figura indicada")  