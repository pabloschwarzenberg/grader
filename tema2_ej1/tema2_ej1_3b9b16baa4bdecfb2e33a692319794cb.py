import math 
def area_triangulo(base,altura):
  base=int(base)
  altura=int(altura)
  area=(base*altura)/2
  return area 

def area_rectangulo(base,altura):
  base=int(base)
  altura=int(altura)
  area=base*altura
  return area

def area_rombo(diagonal1,diagonal2):
    diagonal1=int(diagonal1)
    diagonal2=int(diagonal2)
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    radio=int(radio)
    a=math.pi
    area=a*(radio**2)
    return area

if __name__ == "__main__":
    menu=int(input("ingrese el area: "))
    if menu==1:
        print(area_triangulo)
    elif menu==2:
        print(area_rectangulo)
    elif menu==3:
        print(area_rombo)
    elif menu==4:
        print(area_circulo)