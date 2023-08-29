import math
def area_triangulo(base,altura):

   if base > 0 and altura > 0 :
        w=(base*altura)/2
        return w
       
def area_rectangulo(base,altura):

   if base > 0 and altura > 0:
        w = base * altura
        return w
       
def area_rombo(diagonal1,diagonal2):

    if diagonal1 > 0 and diagonal2 > 0:
        w = (diagonal1 * diagonal2)/2
        return w

def area_circulo(radio):
   
   if radio >0 :
        w=math.pi*(radio**2)
        return w


    
           