import math as m
def area_triangulo(base,altura):
  AreaT = (base * altura)/2      
    return AreaT

def area_rectangulo(base,altura):
    AreaR = base * altura 

def area_rombo(diagonal1,diagonal2):
  Arearb = (diagonal1*diagonal)/2 
    

def area_circulo(radio):
  AreaC = m.pi * (radio**2)
    

if __name__ == "__main__":
  a = input("ingrese la figura que quiere calcular")
  a.lower = a
  if a == "triangulo":
    base = int(input("ingrese la base"))
    altura = int(input("ingrese la altura"))
    print(area_triangulo(AreaT))
  elif a == "rectangulo":
    base = int(input("ingrese la base"))
    altura = int(input("ingrese la altura"))
    print(area_rectangulo(AreaR))
  elif a == "rombo":
    diagonal1 = int(input("ingrese la diagonal 1"))
    diagonal2 = int(input("ingrese la diagonal 2"))
    print(area_rombo(Arearb))
  elif a == "circulo"
    radio = int(input("ingrese el radio"))
    print(area_circulo(AreaC))
  else:
    input("Tu figura no esta en esta calculadora")
  
  
    
           