import math

def area_triangulo(base,altura):
    a = (base*altura)/2
    
    return a
  

def area_rectangulo(base,altura):
    b = (base*altura)
    
    return b

def area_rombo(diagonal1,diagonal2):
    c = (diagonal1*diagonal2)/2
    
    return c

def area_circulo(radio):
    d = math.pi*radio**2
    
    return d

if __name__ == "__main__":

  cac = int(input("Que area desea calcular:"))

  if (cac == 1):

    it = float(input("Cual es la base? "))
    h = float(input("Cual es la altura? "))

    print(area_triangulo(it,h))
  
  elif(cac == 2):

    ir = float(input("Cual es la base? "))
    h = float(input("Cual es la altura? "))

    print(area_rectangulo(ir,h))  
  
  elif(cac == 3):

    d1 = float(input("Cual es la diagonal 1?"))
    d2 = float(input("Cual es la diagonal 2?"))

    print(area_rombo(d1,d2))

  elif(cac == 4):

    r = float(input("Cual es el radio?"))

    print(area_circulo(r))

  
      
           