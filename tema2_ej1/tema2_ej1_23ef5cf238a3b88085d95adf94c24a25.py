import math
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area
def area_rectangulo(base,altura):
    area = base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area = math.pi*radio**2
    return area
if __name__ == "__main__":
    opcion=int(input("""(1)Triangulo
    (2)Rectangulo
    (3)Rombo
    (4)Circulo
    Seleccione la figura que quiere calcular su area: """))
    if opcion==1:
      base=int(input("Ingrese base triangulo: "))
      altura=int(input("Ingrese altura triangulo: "))
      print(area_triangulo(base,altura))
    elif opcion==2:
      base=int(input("Ingrese base rectangulo: "))
      altura=int(input("Ingrese altura rectangulo: "))
      print(area_rectangulo(base,altura))
    elif opcion==3:
      diagonal1=int(input("Ingrese valor diagonal: "))
      diagonal2=int(input("Ingrese valor otra diagonal: "))
      print(area = (diagonal1*diagonal2)/2)
    elif opcion==4:
      radio=int(input("Ingrese radio circulo: "))
      print(area_circulo(radio))
    