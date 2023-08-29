import math
def area_triangulo(base,altura):
    at=base*altura/2
    return at

def area_rectangulo(base,altura):
    are=base *altura
    return are

def area_rombo(diagonal1,diagonal2):
    aro=diagonal1*diagonal2/2
    return aro

def area_circulo(radio):
    pi=math.pi
    ac=pi*radio**2 
    return ac
    
if __name__ == "__main__": 
   figura=int(input("ingrese un numero:"))
   if figura==1:
       base=int(input("i"))
       altura=int(input("i"))
       print(area_triangulo(base,altura))
   if figura==2:
       base=int(input("i"))
       altura=int(input("i"))
       print(area_rectangulo(base,altura))
   if figura==3:
       diagonal1=int(input("i"))
       diagonal2=int(input("i"))
       print(area_rombo(diagonal1,diagonal2))
   if figura==4:
       radio=int(input("i"))
       print(area_circulo(radio))