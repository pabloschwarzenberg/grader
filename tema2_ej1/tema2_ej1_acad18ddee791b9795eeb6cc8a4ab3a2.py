import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=(base*altura)
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area 
def area_circulo(radio):
     area=math.pi*(radio)**2
     return area
     
if __name__ == "__main__":
   a=int(input("accion: "))
   if a==1:
    base=float(input("base:"))
    altura=float(input("altura: "))
    area_triangulo(base,altura)
   elif a==2:
     base=float(input("base:"))
     altura=float(input("altura: "))
     area_rectangulo(base,altura)
   
   elif a==3:
      diagonal1=float(input("base:"))
      diagonal2=float(input("altura: "))
      area_rombo(diagonal1,diagonal2)
   elif a==4:
     radio=float(input("radio:"))
     area_circulo(radio)