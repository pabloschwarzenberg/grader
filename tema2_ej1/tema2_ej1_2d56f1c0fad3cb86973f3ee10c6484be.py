import math
math.pi
def area_triangulo(base,altura):
    t=(base*altura)/2
    return(t)
    

def area_rectangulo(base,altura):
    r=base*altura
    return(r)
    

def area_rombo(diagonal1,diagonal2):
    ro=(diagonal1*diagonal2)/2
    return(ro)
    

def area_circulo(radio):
    c=math.pi*radio*radio
    return(c)
     

if __name__ == "__main__":
    d=input("ingrese la figura:")
    if d=="triangulo":
      if __name__ == "__main__":
        base=int(input("ingrese base :"))
        altura=int(input("ingrese altura :"))
        area_triangulo(base,altura)
        
    elif d=="rectangulo":
      if __name__ == "__main__":
        base=int(input("ingrese base del rectangulo:"))
        altura=int(input("ingrese altura del ractangulo:"))
        area_rectangulo(base,altura)
    elif d=="rombo":
      if __name__ == "__main__":
        diagonal1=int(input("ingrese diagonal1:"))
        diagonal2=int(input("ingrese diagonal2:"))
        area_rombo(diagonal1,diagonal2)
    elif d=="circulo":
      if __name__ == "__main__":
        radio=int(input("ingrese radio:"))
        area_circulo(radio)    
    
