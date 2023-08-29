def area_triangulo(base,altura):
    areatriangulo=(base*altura)/2
    return areatriangulo

def area_rectangulo(base,altura):
    arearectangulo=base*altura
    return arearectangulo

def area_rombo(diagonal1,diagonal2):
    arearombo=(diagonal1*diagonal2)/2
    return arearombo

def area_circulo(radio):
    import math
    areacirculo=(math.pi*radio*radio)
    return areacirculo

if __name__ == "__main__":
    opcion=int(input("Ingrese la opcion a calcular el area:"))
    if opcion==1:
      base=int(input("Ingrese base:"))
      altura=int(input("Ingrese altura:"))
      print(area_triangulo(base,altura))
    if opcion==2:
      base=int(input("Ingrese base:"))
      altura=int(input("Ingrese altura:"))
      print(area_rectangulo(base,altura))
    if opcion==3:
      diagonal1=int(input("Ingrese diagonal1:"))
      diagonal2=int(input("Ingrese diagonal2:"))
      print(area_rombo(diagonal1,diagonal2))
    if opcion==4:
      radio=int(input("Ingrese el radio:"))
      print(area_circulo(radio))
           