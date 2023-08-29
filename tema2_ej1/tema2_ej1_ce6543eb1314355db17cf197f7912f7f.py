import math

def area_triangulo(base,altura):
    area= base*altura/2
    return area

def area_rectangulo(base1,altura1):
    area_Re= base1*altura1
    return area_Re
    
def area_rombo(diagonal1,diagonal2):
    area_R= diagonal1*diagonal2/2
    return area_R

def area_circulo(radio):
    area_C=math.pi*radio**2
    return area_C
    
    
menude_areas=input("\telija el area de la figura geometrica que desea calcular:  \n1.rectangulo \n2.triangulo \n3.rombo \n4.circulo \n")  
while menude_areas != 0:
      if(menude_areas == 1):
           base1=  float(input("ingrese la base del rectangulo:"))
           altura1= float(input("ingrese la altura del rectangulo:"))
           print("area del rectangulo",round(area_rectangulo(base1,altura1),2))
      elif(menude_areas == 2):
          base=  float(input("ingrese la base del triangulo:"))
          altura= float(input("ingrese la altura del triangulo:"))
          print("area del triangulo",round(area_triangulo(base,altura),2))
         
      elif(menude_areas == 3):
           diagonal1=  float(input("ingrese la diagonal 1 del rombo:"))
           diagonal2= float(input("ingrese la diagonal 2 rombo:"))
           print("area del rombo",round(area_rombo(diagonal1,diagonal2),2))
      elif(menude_areas == 4):
           radio=  float(input("ingrese el radio del circulo:"))
           print("areadel circulo",round(area_circulo(radio),2))
      menude_areas=int(input("elija el area de la figura geometrica que desea calcular: \n1.triangulo \n2.rectangulo \n3.rombo \n4.circulo \n"))   

pass