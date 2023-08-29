import math
def area_triangulo(b,c):
    return((b*c)/2)

def area_rectangulo(b,c):
    return(b*c)
    
def area_rombo(b,c):
    return((b*c)/2)
       
def area_circulo(b):
    return (math.pi*(b**2))
   
if __name__ == "__main__":

  a=str(input())
  if a== "triangulo":
       b=float(input())
       c=float(input())
       print(area_triangulo(b,c))
       
  elif a== "rectangulo":
       b=float(input())
       c=float(input())
       print(area_rectangulo(b,c))
       
  elif a== "rombo":
       b=float(input())
       c=float(input())
       print(area_rombo(b,c))
       
  elif a== "circulo":
       b=float(input())
       print(area_circulo(b))





    
           