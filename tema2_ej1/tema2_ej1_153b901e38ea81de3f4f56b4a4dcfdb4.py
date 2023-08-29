import math
def area_triangulo(base,altura):  
  base=int(base) 
  altura=int(altura) 
  areat=float((base*altura)/2) 
  return areat 

def area_rectangulo(base,altura): 
  base=int(base) 
  altura=int(altura) 
  areare=base*altura 
  return areare

def area_rombo(diagonal1,diagonal2): 
  diagonal1=int(diagonal1) 
  diagonal2=int(diagonal2) 
  arearo=(diagonal1*diagonal2)/2 
  return arearo

def area_circulo(radio): 
  radio=int(radio) 
  areac=math.pi*(radio**2) 
  return areac


if __name__ == "__main__": 
  figura=input("Que area desea calcular?")  
  if figura==triangulo: 
    base=int(input("Ingrese la base")) 
    altura=int(input("Ingrese la altura")) 
    print(area_triangulo(base,altura)) 
  elif figura==rectangulo: 
    base=int(input("Ingrese la base")) 
    altura=int(input("Ingrese la altura")) 
    print(area_rectangulo(base,altura)) 
  elif figura==rombo: 
    diagonal1=int(input("Ingrese la diagonal 1")) 
    diagonal2=int(input("Ingrese la diagonal 2")) 
    print(area_rombo(diagonal1,diagonal2)) 
  elif figura==circulo: 
    radio=int(input("Ingrese el radio")) 
    print(area_circulo(radio))

           