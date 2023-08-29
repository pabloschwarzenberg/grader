#Aprobación de créditos
Ingreso=int(input())
Nacimiento=int(input())
Hijos=int(input())
Pertenencia=int(input())
Civil=str(input())
Lugar=str(input())
if Pertenencia>10:
   if Hijos>=2:
      print("APROBADO")
if Civil=="C":
   if Hijos>3:
      if 1963<Nacimiento<1973:
         print("APROBADO")
if Ingreso>2500000:
   if Civil==S:
      if Lugar==U:
         print("APROBADO")
if Ingreso>3500000:
    if Pertenencia>5:
       print("APROBADO")
if Lugar=="R":
   if Civil=="C":
      if Hijos<2:
         print("APROBADO")