import math 

def area_triangulo(base,altura):
    return base * altura /2 

def area_rectangulo(base,altura):
    return base * altura 

def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 /2

def area_circulo(radio):
    return radio * radio * math.pi 

if __name__ == "__main__":
  Ope =int(input("introduzca numero de opercion que desea realizar: 1=Triangulo 2= rectangulo 3=Rombo 4=Circulo"))
  if 1 == Ope:
      Base = float(input("ingrese la base del triangulo"))
      Altura = float(input("ingrese la altura del triangulo"))
      print (area_triangulo(Base,Altura))
    
  elif 2 == Ope:
     Base = float(input("ingrese la base del rectangulo "))
     Altura = float(input("ingrese la altura del rectangulo"))
     print (area_rectangulo(Base,Altura))
    
  elif 3 == Ope:
     Diagonal1 = float(input("ingrese la diagonal 1 rombo "))
     Diagonal2 = float(input("ingrese la diagonal 2 rombo "))
     print (area_rombo(Diagonal1,Diagonal2))
    
  elif 4 == Ope:
     Radio = float(input("ingrese el radio de la circunferencia"))
     print (area_circulo(Radio))
     
    
    
    
    