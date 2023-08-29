import math
def area_triangulo(base,altura):
    A=(base*altura)/2
    return A
    pass

def area_rectangulo(base,altura):
    A=base*altura
    return A
    pass

def area_rombo(diagonal1,diagonal2):
    A=diagonal1*diagonal2/2
    return A
    pass

def area_circulo(radio):
    A=math.pi*(radio**2)
    return A
    pass

if __name__ == "__main__":
    
  print("¿Que area desea escoger?")
  print("1) triangulo")
  print("2) rectangulo")
  print("3) rombo")
  print("4) circulo")
  opcion=int(input())
  if opcion==1:
    base=int(input())
    altura=int(input())
    A=area_triangulo(base,altura)
    print(A)
  elif opcion==2:
    base=int(input())
    altura=int(input())
    A=area_rectangulo(base,altura)
    print(A)
  elif opcion==3:
    diagonal1=int(input())
    diagonal2=int(inou())
    A=area_rombo(diagonal1,diagonal2)
    print(A)
  elif opcion==4:
    radio=int(input())
    A=area_circulo(radio)
    print=(A)