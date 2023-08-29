import math

def area_triangulo(base,altura):
    base=float(base)
    altura=float(altura)
    
    area=(base*altura)/2
    
    return area

def area_rectangulo(base,altura):
    base=float(base)
    altura=float(altura)
  
    area=base*altura
  
    return area
  
   

def area_rombo(diagonal1,diagonal2):
    diagonal1=float(diagonal1)
    diagonal2=float(diagonal2)
    
    area=(diagonal1*diagonal2)/2
    
    return area

def area_circulo(radio):
    radio=float(radio)
    
    area=math.pi*(radio**2)
    
    return area

if __name__ == "__main__":
  base=float(input())
  altura=float(input())
  area=input()
  
  if area=="rectangulo":
    print(area_rectangulo(base,altura))
    
  if area=="triangulo":
    print(area_triangulo(base,altura))
  if area=="rombo":
    print(area_rombo(base,altura))
    
  if area=="circulo":
    print(area_circulo(base))
    
           