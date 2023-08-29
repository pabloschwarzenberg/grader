import math

def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
  

def area_rectangulo(base,altura):
    area=base*altura
    return area
    

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
    

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area


if __name__ == "__main__":
    
  print("Que area desea calcular?:\n1)Triangulo \n2)Rectangulo \n3)Rombo \n4)circulo\n")
  opcion=int(input())
  if opcion==1:
    base=int(input())
    altura=int(input())
    print(area_triangulo(base,altura))
    
  elif opcion==2:
    base=int(input())
    altura=int(input())
    print(area_rectangulo(base,altura))
  elif opcion==3:
    diagonal1=int(input())
    diagonal2=int(input())
    print(area_rombo(diagonal_mayor,diagonal_menor))
  elif opcion==4:
    radio=int(input())
    print(area_circulo(radio))