ingreso=int(input("Ingrese sus sueldo:"))
nacimiento=int(input("ingrese su año de nacimiento:"))
h=int(input("ingrese su cantidad de hijos/as:"))
anosen=int(input("ingrese su cantidad de años en el banco:"))
print("C=0,1,S=0,2,U=0,3,R=0,4")
C=0,1
S=0,2
U=0,3
R=0,4
estado=(input("ingrese su estado civil C/S:"))
if(0,2==estado or estado==0,1):
  pass
domicilio=(input("Urbano o Rural U/R:"))
if(0,4==domicilio>=0,3):
  pass
if ((h>=2) and (anosen>=10)):
 print("APROBADO")
elif(estado==0,1 and h>3 and (55>2020-nacimiento>45)):
 print("APROBADO")
elif ((ingreso>2500000) and estado==0,2 and domicilio==0,3):
 print("APROBADO")
elif (ingreso>3500000 and anosen>5):
 print("APROBADO")
elif(domicilio==0,3 and estado==0,1 and h<2):
  print("APROBADO")
else:
  print("Se rechaza el credito")   