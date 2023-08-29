from math import pi
def area_triangulo(base,altura):
  return((base*altura)/2)

def area_rectangulo(base,altura):
  return(base*altura)

def area_rombo(diagonal1,diagonal2):
  return((diagonal1*diagonal2)/2)

def area_circulo(radio):
  return(pi*radio**2)


  opcion=int(input("Ingrese una opcion; 0.Cancelar,1.Triangulo,2.Rectangulo,3.Rombo,4.Circulo "))
  while(opcion==0):
    print("Hasta la proxima")
    break
  while(opcion==1):
    base=float(input("Ingrese la base:"))
    altura=float(input("Ingrese la altura:"))
    print(area_triangulo(base,altura))
    break
  while(opcion==2):
    base=float(input("Ingrese la base:"))
    altura=float(input("Ingrese la altura:"))
    print(area_rectangulo(base,altura))
    break
  while(opcion==3):
    diagonal1=float(input("Ingrese primera diagonal:"))
    diagonal2=float(input("Ingrese segunda diagonal:"))
    print(area_rombo(diagonal1,diagonal2))
    break
  while(opcion==4):
    radio=float(input("Ingrese el radio del circulo:"))
    print(area_circulo(radio))
    break
