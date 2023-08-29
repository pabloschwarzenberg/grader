#Aprobación de créditos
ingreso=int(input("ingrese en pesos $"))
edad=input("ingrese edad: ")
num_hijos=int(input("Ingrese numero de hijos: "))
años_en_el_Banco=int(input("ingrese años de pertenencia en el Banco: "))
estado_civil=input("ingrese estado civil:(soltero (S) casado (C)): ")
donde_vive=input("ingrese donde vive urbano (U), rural(R) : ")
contador=0
#Opion 1

if años_en_el_Banco>10 and num_hijos>=2:
  contador=contador+1
  print("APROBADO CREDITO 1")
  
#Opcion 2

if  num_hijos>=3:
  if edad >= "45" or edad <= "55":
    if estado_civil.upper() == "C":
      contador=contador+1
      print("APROBADO CREDITO 2")

#Opcion 3
if ingreso>=2500000:
  if estado_civil.upper()=="S": 
      if donde_vive.upper()=="U": 
        contador=contador+1
        print("APROBADO CREDITO 3")

#Opcion 4

if ingreso>=3500000:
   if años_en_el_Banco>5:
     contador=contador+1
     print("APROBADO CREDITO 4")

#Opcion 5
if donde_vive.upper()=="R":
  if estado_civil.upper()=="C":
    if num_hijos<2:
      contador=contador+1
      print("APROBADO CREDITO 5")
  
else:
  ("RECHAZADO")
print("Creditos Aprobados ",contador)