import math
math.pi
def area_triangulo(base,altura):
 a=base*altura
 b=a/2
 return b

def area_rectangulo(base,altura):
  c=base*altura
  return c
   

def area_rombo(diagonal1,diagonal2):
  d=diagonal1*diagonal2
  f=d/2
  return f
   

def area_circulo(radio):
  e=math.pi*radio**2
  return e
    

if __name__ == "__main__":
  figura=intput("a que figura le quiere sacar el area?  ")
  if figura=="triangulo":
    base=int(input)
    altura=int(input)
    area_triangulo(base,altura)
  elif figura=="rectangulo":
    base=int(input)
    altura=int(input)
    area_rectangulo(base,altura)
  elif figura=="rombo":
    diagonal=int(input)
    diagonal2=int(input)
    area_rombo(diagonal1,diagonal2)
  elif figura=="circulo":
    radio=int(input)
    area_circulo(radio)





 
           