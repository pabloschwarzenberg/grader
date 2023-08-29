def area_triangulo():
 base=int(input("ingrese base: "))
 altura=int(input("ingrese altura: "))
 area=(base*altura)/2
 return(area)
def area_rectangulo():
 base=int(input("ingrese base: "))
 altura=int(input("ingrese altura: "))
 area=(base*altura)
 return(area)
def area_rombo():
 diagonal1=int(input("ingrese diagonal 1:"))
 diagonal2=int(input("ingrese diagonal 2:"))
 area=(diagonal1*diagonal2)/2
 return(area)
import math
pi=math.pi
def area_circulo():
 radio=int(input("Ingresa el radio:"))
 area=(pi*(radio**2))
 return(area)
  
opcion=0
while(opcion==0):
 print("1.triángulo")
 print("2.rectangulo")
 print("3.rombo")
 print("4.círculo")
 print("5.salir")
 opcion=int("Que área desea calcular: ")
 if(opcion==1):
   area1=area_triangulo()
   print(area1)
   opcion=0
 if(opcion==2):
   area2=area_rectangulo()
   print(area2)
   opcion=0
 if(opcion==3):
   area3=area_rombo()
   print(area3)
   opcion=0
 if(opcion==4):
   area4=area_circulo()
   print(area4)
   opcion=0
 if(opcion==5):
   print("adiós")