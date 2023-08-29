import math
def area_triangulo(base,altura):
  areatriangulo=(base*altura)/2
  return areatriangulo
  pass

def area_rectangulo(base,altura):
  arearectangulo=base*altura
  return arearectangulo
  pass

def area_rombo(diagonal1,diagonal2):
  arearombo=(diagonal1*diagonal2)/2
  return arearombo
  pass

def area_circulo(radio):
  areacirculo=math.pi*radio*radio
  return areacirculo
  pass
  

if __name__ == "__main__":
  opcion=input("Escoja la figura a la que desea calcular su area: ")
  opcion2=opcion.lower()

  if opcion2=="triangulo":
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    print(area_triangulo(base,altura))

  elif opcion2=="rectangulo":
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    print(area_rectangulo(base,altura))
  
  elif opcion2=="rombo":
    diagonal1=int(input("Diagonal 1: "))
    diagonal2=int(input("Diagonal 2: "))
    print(area_rombo(diagonal1,diagonal2))
  
  elif opcion2=="circulo":
    radio=int(input("Radio: "))
    print(area_circulo(radio))
  pass 