#Aprobación de créditos
ingreso=int(input("ingrese los ingresos en pesos:"))
nacimiento=int(input("ingrese el año de nacimiento:"))
hijos=int(input("ingrese el número de hijos:"))
anosbanco=int(input("ingrese los años de pertenencia al banco:"))
estado=input("inrese el estado civil (S:soltero, C:casado):")
vive=input("vive en (U:urbano, R:rural):")
edad=2020-nacimiento
if anosbanco>10 and 2<=hijos:
 print("APROBADO")
else:
 if estado=="C" and 3<hijos and 45<=edad<=55:
  print("APROBADO")
 else:
  if ingreso>3500000 and anosbanco>5:
   print("APROBADO")
  else:
   if vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
   else:

    print("RECHAZADO")

