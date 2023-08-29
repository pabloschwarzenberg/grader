import math
def area_triangulo(base,altura):
  area=(base*altura)/2
  return area

def area_rectangulo(base,altura):
  area=base*altura
  return area

def area_rombo(diagonal1,diagonal2):
  area=diagonal1*diagonal2
  return area

def area_circulo(radio):
  x=math.pi
  area=x*pow(radio,2)
  return area
seleccion=eval(input("ingresa el area que quieres trabajar"))
if(seleccion==1):
  base=eval(input("ingresa base"))
  altura=eval(input("ingresa altura"))
  area_triangulo(base,altura)    
elif(seleccion==2):
  base=eval(input("ingresa base"))
  altura=eval(input("ingresa altura"))
  area_rectangulo(base,altura)
elif(seleccion==3):
  diagonal1=eval(input("ingresa diagonal1"))
  diagonal2=eval(input("ingresa diagonal2"))
  area_rombo(diagonal1,diagonal2)
elif(seleccion==4):
  radio=eval(input("ingresa radio"))
  area_circulo(radio)
           
           