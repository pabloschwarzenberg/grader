import math

def area_triangulo(base,altura):
    a=base*altura
    b=a/2
    return b

def area_rectangulo(base,altura):
    ar=base*altura
    return ar
    
    
def area_rombo(diagonal1,diagonal2):
    arb=diagonal1*diagonal2
    c=arb/2
    return c
    

def area_circulo(radio):
    a=radio*radio*math.pi
    return a 
    

if __name__ == "__main__":
  opcion=0
  print("(1)Area triangulo\n(2)Area rectangulo\n(3)Area rombo\n(4)Area circulo")
  opcion=int(input("Que opcion eligues?"))

  if opcion==1:
    base=int(input("Ingrese la base:"))
    altura=int(input("Ingrese la altura:"))        
    print(area_triangulo(base,altura))

  if opcion==2:
    base=int(input("Ingrese la base:"))
    altura=int(input("Ingrese la altura:"))
    print(area_rectangulo(base,altura))
  
  if opcion==3:
    diagional1=int(input("Ingrese diagonal 1:"))
    diagonal2=int(input("Ingrese diagonal 2:"))
    print(area_rombo(diagonal1,diagonal2))

  if opcion==4:
    radio=int(input("Ingrese radio:"))
    print(area_circulo(radio))
   
    
           