#Aprobación de créditos
INGRE=int(input("ingrese sueldo: "))
NACI=int(input("ingrese fecha de nacimiento: "))
HIJOS=int(input("ingrese N de hijos: "))
PERM=int(input("ingrese años de permanencia: "))
ESTC=input("ingrese su estado civil: ")
LUG=input("ingrese si vive en campo o ciudad: ")
if (PERM>10 and HIJOS>=2):
  print("APROBADO")
if(ESTC=="C" and HIJOS>3 and 2022-NACI>=45 and 2022-NACI<=55):
  print("APROBADO")
if(INGRE>2500000 and ESTC=="S" and LUG=="U"):
  print("APROBADO")
if(INGRE>3500000 and PERM>5):
  print("APROBADO")
if(LUG=="R" and ESTC=="C" and HIJOS<2):
  print("APROBADO")
else:
  print("RECHAZADO")