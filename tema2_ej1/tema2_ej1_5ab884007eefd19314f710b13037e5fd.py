import math
def area_triangulo(base,altura):
  area=float(base)*float(altura)/2
  return area
  pass

def area_rectangulo(base,altura):
  area=float(base)*float(altura)
  return area
  pass

def area_rombo(diagonal1,diagonal2):
  area=float(diagonal1)*float(diagonal2)/2
  return area
  pass

def area_circulo(radio):
  area=float(radio)*float(radio)*math.pi
  return area
  pass
if __name__=="__main__":
    q=int(input( ))
    if q==1:
      a=input()
      b=input()
      area_triangulo(a,b)
    elif q==2:
      a=input()
      b=input()
      area_rectangulo(a,b)
    elif q==3:
      a=input()
      b=input()
      area_rombo(a,b)
    elif q==4:
      a=input()
      area_circulo(a)