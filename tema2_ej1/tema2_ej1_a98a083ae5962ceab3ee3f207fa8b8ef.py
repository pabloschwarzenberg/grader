import math

def area_triangulo(base,altura):
    area=base*altura
    area=area/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(d1,d2):
  area = d1 * d2
  area = area / 2
  return area

def area_circulo(radio):
    radio=radio*radio
    area=(math.pi)*radio
    return area

if __name__ == "__main__":
    print("""Ingrese el numero correspondiente a la figura a la cual desea calcular area:
    -Triangulo (1)
    -Rectangulo (2)
    -Rombo (3)
    -Circulo (4)
    """)
    opcion=int(input("Opción:"))

    if opcion==1:
      base=int(input("Ingrese base del triangulo:"))
      altura=int(input("Ingrese altura del triangulo:"))
      print(area_triangulo(base,altura))
    
    if opcion == 2:
      base = int(input("Ingrese base:"))
      altura = int(input("Ingrese altura:"))
      print(area_rectangulo(base,altura))
    
    if opcion == 3:
      d1 = int(input("Ingrese diagonal 1:"))
      d2 = int(input("Ingrese diagonal 2:"))
      print(area_rombo(d1, d2))
    
    if opcion == 4:
      radio=int(input("Ingrese radio del circulo:"))
      print(area_circulo(radio))
