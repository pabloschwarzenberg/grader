def area_triangulo(base,altura):
    a=((base*altura)/2)
    return a

def area_rectangulo(base,altura):
    b=(base*altura)
    return b

def area_rombo(diagonal1,diagonal2):
    c=((diagonal1*diagonal2)/2)
    return c

def area_circulo(radio):
    import math
    d=(math.pi*radio**2)
    return d

if __name__ == "__main__":
     base=int(input())
     altura=int(input())
     diagonal1=int(input())
     diagonal2=int(input())
     radio=int(input())
  
  
   
           